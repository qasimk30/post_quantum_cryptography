from secrets import compare_digest
from pqcrypto.kem.mceliece8192128 import generate_keypair as gen_kem, encrypt, decrypt
from pqcrypto.sign.sphincs_shake_256s_simple import generate_keypair as gen_sig, sign, verify

# KEM
def generate_kem_keys():
    return gen_kem()

def encrypt_message(public_key):
    ciphertext, plaintext = encrypt(public_key)
    return ciphertext, plaintext

def decrypt_message(secret_key, ciphertext):
    return decrypt(secret_key, ciphertext)

# Signature
def generate_sig_keys():
    return gen_sig()

def sign_message(secret_key, message: bytes):
    return sign(secret_key, message)

def verify_signature(public_key, message: bytes, signature):
    return verify(public_key, message, signature)
