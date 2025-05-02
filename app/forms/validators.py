"""
Custom validators for form fields
"""
from wtforms.validators import ValidationError

def validate_hex(form, field):
    """Validate that the field contains a valid hex string"""
    try:
        # Check if empty
        if not field.data:
            return
        
        # Attempt to convert from hex
        bytes.fromhex(field.data)
    except ValueError:
        raise ValidationError('Field must contain a valid hexadecimal string')