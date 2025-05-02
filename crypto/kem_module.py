from kyber_py.kyber import Kyber512

def generate_keypair():
    """
    Generate a Kyber KEM keypair using kyber_py.
    
    Returns:
        tuple: (public_key, private_key)
    """
    return Kyber512.keygen()

def encapsulate(public_key):
    """
    Encapsulate a shared secret using a public key.
    
    Args:
        public_key (bytes): The public key.
        
    Returns:
        tuple: (ciphertext, shared_secret)
    """
    shared_secret, ciphertext = Kyber512.encaps(public_key)
    return ciphertext, shared_secret

def decapsulate(ciphertext, private_key):
    """
    Decapsulate a shared secret using a ciphertext and private key.
    
    Args:
        ciphertext (bytes): The ciphertext.
        private_key (bytes): The private key.
        
    Returns:
        bytes: The shared secret.
    """
    return Kyber512.decaps(private_key, ciphertext)
