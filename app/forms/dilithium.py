"""
Forms for Dilithium signature operations
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

from app.forms.validators import validate_hex

class DilithiumSignForm(FlaskForm):
    """Form for Dilithium signing"""
    private_key = StringField('Private Key', validators=[
        DataRequired(),
        validate_hex
    ])
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=1, max=1000)
    ])

class DilithiumVerifyForm(FlaskForm):
    """Form for Dilithium signature verification"""
    public_key = StringField('Public Key', validators=[
        DataRequired(),
        validate_hex
    ])
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=1, max=1000)
    ])
    signature = StringField('Signature', validators=[
        DataRequired(),
        validate_hex
    ])