"""
Routes for Dilithium signature operations
"""
from flask import Blueprint, render_template, request, jsonify

import crypto.signature_module as dilithium
from app.forms import DilithiumSignForm, DilithiumVerifyForm
from app import csrf

# Create blueprint
dilithium_bp = Blueprint('dilithium', __name__)

@dilithium_bp.route('/dilithium')
def dilithium_demo():
    """Render the Dilithium signature demonstration page"""
    return render_template('signature.html', algo_name="Dilithium Signature", algo_type="Signature")

@dilithium_bp.route('/api/dilithium/generate', methods=['POST'])
@csrf.exempt
def dilithium_keygen():
    """
    Generate a new Dilithium keypair
    
    Returns:
        JSON with public and private keys in hex format
    """
    try:
        # Generate new Dilithium keypair
        pk, sk = dilithium.generate_keypair()
        
        # Return success response
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

@dilithium_bp.route('/api/dilithium/sign', methods=['POST'])
@csrf.exempt
def dilithium_signing():
    """
    Create a signature for a message using Dilithium
    
    Takes:
        private_key: Hex-encoded Dilithium private key
        message: UTF-8 message to sign
        
    Returns:
        JSON with signature in hex format
    """
    try:
        # Create form for validation
        form = DilithiumSignForm(meta={'csrf': False})
        
        # If form data is provided via form fields
        if request.form:
            form = DilithiumSignForm(request.form)
        # If JSON data is provided
        elif request.json:
            form = DilithiumSignForm(data=request.json)
            
        # Validate the data
        if not form.validate():
            return jsonify({
                'status': 'error',
                'message': 'Invalid input data',
                'errors': form.errors
            }), 400
            
        # Get data from validated form
        sk_hex = form.private_key.data
        message = form.message.data
        
        # Convert key from hex and message to bytes
        sk_bytes = bytes.fromhex(sk_hex)
        message_bytes = message.encode('utf-8')
        
        # Create signature
        signature = dilithium.sign(message_bytes, sk_bytes)
        
        # Return success response
        return jsonify({
            'status': 'success',
            'signature': signature.hex()
        })
    except Exception as e:
        # Return error response
        return jsonify({
            'status': 'error', 
            'message': str(e)
        })

@dilithium_bp.route('/api/dilithium/verify', methods=['POST'])
@csrf.exempt
def dilithium_verification():
    try:
        data = request.get_json()
        public_key, signature_key = dilithium.generate_keypair()
        message = data.get('message', '').encode('utf-8')
        print(type(message))

        sig = dilithium.sign(message, signature_key)

        # Perform verification
        is_valid = dilithium.verify(message, sig, public_key)

        return jsonify({'status': 'success', 'valid': is_valid})

    except ValueError as ve:
        return jsonify({'status': 'error', 'message': f'Hex conversion error: {ve}'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
