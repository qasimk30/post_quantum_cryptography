from dilithium_py.ml_dsa import ML_DSA_44

def generate_keypair():
    """
    Generate a Dilithium signature keypair using ML_DSA_44

    Returns:
        tuple: (public_key, private_key)
    """
    return ML_DSA_44.keygen()

def sign(message, private_key):
    """
    Sign a message using a private key

    Args:
        message (bytes): The message to sign
        private_key (bytes): The private key

    Returns:
        bytes: The signature
    """
    return ML_DSA_44.sign(private_key, message)

def verify(message, signature, public_key):
    """
    Verify a signature using a message and public key

    Args:
        message (bytes): The message that was signed
        signature (bytes): The signature
        public_key (bytes): The public key

    Returns:
        bool: True if signature is valid, False otherwise
    """
    try:
        return ML_DSA_44.verify(public_key, message, signature)
    except Exception:
        return False
