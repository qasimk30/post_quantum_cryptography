from flask import Blueprint, render_template, request, jsonify
from .crypto_utils import *

main = Blueprint("main", __name__)
keys = {}  # Global (for demo only)

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
    return jsonify({"ciphertext": ciphertext.hex(), "plaintext": plaintext.hex()})

@main.route("/kem-decrypt", methods=["POST"])
def kem_decrypt():
    if "kem_sec" not in keys or "ciphertext" not in keys:
        return jsonify({"error": "Missing keys or ciphertext."}), 400
    recovered = decrypt_message(keys["kem_sec"], keys["ciphertext"])
    match = compare_digest(keys["plaintext"], recovered)
    return jsonify({"recovered": recovered.hex(), "match": match})

@main.route("/sig-keygen", methods=["POST"])
def sig_keygen():
    pub, sec = generate_sig_keys()
    keys["sig_pub"] = pub
    keys["sig_sec"] = sec
    return jsonify({"public_key": pub.hex()})

@main.route("/sign", methods=["POST"])
def sign_msg():
    msg = request.form.get("message", "").encode()
    signature = sign_message(keys["sig_sec"], msg)
    keys["signature"] = signature
    return jsonify({"signature": signature.hex()})

@main.route("/verify", methods=["POST"])
def verify_msg():
    msg = request.form.get("message", "").encode()
    result = verify_signature(keys["sig_pub"], msg, keys["signature"])
    return jsonify({"valid": result})
