"""
Routes for Kyber KEM operations
"""
from flask import Blueprint, render_template, request, jsonify

import crypto.kem_module as kyber
from app.forms import KyberEncapsulateForm, KyberDecapsulateForm
from app import csrf

# Create blueprint
kyber_bp = Blueprint('kyber', __name__)

@kyber_bp.route('/kyber')
def kyber_demo():
    """Render the Kyber KEM demonstration page"""
    return render_template('kem.html', algo_name="Kyber KEM", algo_type="KEM")

@kyber_bp.route('/api/kyber/generate', methods=['POST'])
@csrf.exempt
def kyber_keygen():
    """
    Generate a new Kyber keypair
    
    Returns:
        JSON with public and private keys in hex format
    """
    try:
        # Generate new Kyber keypair
        pk, sk = kyber.generate_keypair()
        
        # Return success response with keys
        return jsonify({
            'status': 'success',
            'public_key': pk.hex(),
            'private_key': sk.hex()
        })
    except Exception as e:
        # Return error response
        return jsonify({
            'status': 'error', 
            'message': str(e)
        })

@kyber_bp.route('/api/kyber/encapsulate', methods=['POST'])
@csrf.exempt
def kyber_encap():
    """
    Encapsulate a shared secret using a Kyber public key
    
    Takes:
        public_key: Hex-encoded Kyber public key
        
    Returns:
        JSON with ciphertext and shared secret in hex format
    """
    try:
        # Create form for validation
        form = KyberEncapsulateForm(meta={'csrf': False})
        
        # If form data is provided via form fields
        if request.form:
            form = KyberEncapsulateForm(request.form)
        # If JSON data is provided
        elif request.json:
            form = KyberEncapsulateForm(data=request.json)
            
        # Validate the data
        if not form.validate():
            return jsonify({
                'status': 'error',
                'message': 'Invalid input data',
                'errors': form.errors
            }), 400
            
        # Get public key from validated form and convert from hex
        pk_hex = form.public_key.data
        pk_bytes = bytes.fromhex(pk_hex)
        
        # Perform encapsulation
        ct, ss = kyber.encapsulate(pk_bytes)
        
        # Return success response
        return jsonify({
            'status': 'success',
            'ciphertext': ct.hex(),
            'shared_secret': ss.hex()
        })
    except Exception as e:
        # Return error response
        return jsonify({
            'status': 'error', 
            'message': str(e)
        })

@kyber_bp.route('/api/kyber/decapsulate', methods=['POST'])
@csrf.exempt
def kyber_decap():
    """
    Decapsulate a shared secret using ciphertext and private key
    
    Takes:
        private_key: Hex-encoded Kyber private key
        ciphertext: Hex-encoded ciphertext
        
    Returns:
        JSON with shared secret in hex format
    """
    try:
        # Create form for validation
        form = KyberDecapsulateForm(meta={'csrf': False})
        
        # If form data is provided via form fields
        if request.form:
            form = KyberDecapsulateForm(request.form)
        # If JSON data is provided
        elif request.json:
            form = KyberDecapsulateForm(data=request.json)
            
        # Validate the data
        if not form.validate():
            return jsonify({
                'status': 'error',
                'message': 'Invalid input data',
                'errors': form.errors
            }), 400
            
        # Get data from validated form and convert from hex
        sk_hex = form.private_key.data
        ct_hex = form.ciphertext.data
        
        sk_bytes = bytes.fromhex(sk_hex)
        ct_bytes = bytes.fromhex(ct_hex)
        
        # Perform decapsulation
        ss = kyber.decapsulate(ct_bytes, sk_bytes)
        
        # Return success response
        return jsonify({
            'status': 'success',
            'shared_secret': ss.hex()
        })
    except Exception as e:
        # Return error response
        return jsonify({
            'status': 'error', 
            'message': str(e)
        })