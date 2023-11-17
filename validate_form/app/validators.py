from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError


def validate_email(field_value):
    email_validator = EmailValidator(message='Invalid email format')
    try:
        email_validator(field_value)
    except ValidationError as e:
        raise ValidationError(str(e))


def validate_phone(field_value):
    phone_validator = RegexValidator(
        regex=r'^\+7\d{10}$',
        message='Phone number must be in the format +7 xxx xxx xx xx'
    )
    try:
        phone_validator(field_value)
    except ValidationError as e:
        raise ValidationError(str(e))


def validate_date(field_value):
    date_validator = RegexValidator(
        regex=r'^\d{2}\.\d{2}.\d{4}$|^\d{4}-\d{2}-\d{2}$',
        message='Date must be in the format DD.MM.YYYY or YYYY-MM-DD'
    )
    try:
        date_validator(field_value)
    except ValidationError as e:
        raise ValidationError(str(e))