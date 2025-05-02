"""
Forms for Kyber KEM operations
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from app.forms.validators import validate_hex

class KyberEncapsulateForm(FlaskForm):
    """Form for Kyber encapsulation"""
    public_key = StringField('Public Key', validators=[
        DataRequired(),
        validate_hex
    ])

class KyberDecapsulateForm(FlaskForm):
    """Form for Kyber decapsulation"""
    private_key = StringField('Private Key', validators=[
        DataRequired(),
        validate_hex
    ])
    ciphertext = StringField('Ciphertext', validators=[
        DataRequired(),
        validate_hex
    ])