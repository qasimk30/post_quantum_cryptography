from flask import Blueprint, render_template, request, jsonify
from .crypto_utils import *
import binascii

main = Blueprint("main", __name__)
keys = {}

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/kem-keygen", methods=["POST"])
def kem_keygen():
    pub, sec = generate_kem_keys()
    keys["kem_pub"] = pub
    keys["kem_sec"] = sec
    return jsonify({"public_key": pub.hex()})

@main.route("/kem-encrypt", methods=["POST"])
def kem_encrypt():
    if "kem_pub" not in keys:
        return jsonify({"error": "Generate keys first."}), 400
    ciphertext, plaintext = encrypt_message(keys["kem_pub"])
    keys["ciphertext"] = ciphertext
    keys["plaintext"] = plaintext
    return jsonify({
        "ciphertext": ciphertext.hex(),
        "plaintext_shared_secret": plaintext.hex()
    })

@main.route("/kem-decrypt", methods=["POST"])
def kem_decrypt():
    if "kem_sec" not in keys or "ciphertext" not in keys:
        return jsonify({"error": "Missing keys or ciphertext."}), 400
    recovered = decrypt_message(keys["kem_sec"], keys["ciphertext"])
    match = compare_digest(keys["plaintext"], recovered)
    return jsonify({
        "recovered_shared_secret": recovered.hex(),
        "match": match
    })

@main.route("/sig-keygen", methods=["POST"])
def sig_keygen():
    pub, sec = generate_sig_keys()
    keys["sig_pub"] = pub
    keys["sig_sec"] = sec
    return jsonify({"public_key": pub.hex()})

@main.route("/sign", methods=["POST"])
def sign_msg():
    data = request.get_json()
    msg = data.get("message", "").encode()
    if "sig_sec" not in keys:
        return jsonify({"error": "Generate signature keys first."}), 400
    signature = sign_message(keys["sig_sec"], msg)
    keys["signature"] = signature
    keys["signed_msg"] = msg
    return jsonify({"signature": signature.hex()})

@main.route("/verify", methods=["POST"])
def verify_msg():
    data = request.get_json()
    msg = data.get("message", "").encode()
    if "sig_pub" not in keys or "signature" not in keys:
        return jsonify({"error": "Generate keys and sign first."}), 400
    result = verify_signature(keys["sig_pub"], msg, keys["signature"])
    return jsonify({"valid": result})
