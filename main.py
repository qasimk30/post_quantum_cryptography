from secrets import compare_digest
from pqcrypto.kem.mceliece8192128 import generate_keypair, encrypt, decrypt

# Alice generates a (public, secret) key pair
public_key, secret_key = generate_keypair()

# Bob derives a secret (the plaintext) and encrypts it with Alice's public key to produce a ciphertext
ciphertext, plaintext_original = encrypt(public_key)

# Alice decrypts Bob's ciphertext to derive the now shared secret
plaintext_recovered = decrypt(secret_key, ciphertext)

# Compare the original and recovered secrets in constant time
assert compare_digest(plaintext_original, plaintext_recovered)


from pqcrypto.sign.sphincs_shake_256s_simple import generate_keypair, sign, verify

# Alice generates a (public, secret) key pair
public_key, secret_key = generate_keypair()

# Alice signs her message using her secret key
signature = sign(secret_key, b"Hello world")

# Bob uses Alice's public key to validate her signature
assert verify(public_key, b"Hello world", signature)