from django.core.validators import EmailValidator, RegexValidator
from django.db import models


class FieldType(models.TextChoices):
    EMAIL = 'email', 'Email'
    PHONE = 'phone', 'Phone'
    DATE = 'date', 'Date'
    TEXT = 'text', 'Text'


class FormData(models.Model):
    id = models.AutoField(primary_key=True)
    email_validator = EmailValidator(message='Invalid email format')
    phone_validator = RegexValidator(
        regex=r'^\+\d{1,3}\s\d{1,5}\s\d{1,5}\s\d{1,2}\s\d{1,2}\s\d{1,2}$',
        message='Phone number must be in the format +7 xxx xxx xx xx'
    )
    date_validator = RegexValidator(
        regex=r'^\d{2}\.\d{2}.\d{4}$|^\d{4}-\d{2}-\d{2}$',
        message='Date must be in the format DD.MM.YYYY or YYYY-MM-DD'
    )
    name_field = models.CharField(max_length=255, blank=True, null=True)
    field_type = models.CharField(max_length=255, choices=FieldType.choices, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def clean(self):
        if self.field_type == 'email':
            validators = [self.email_validator]
        elif self.field_type == 'phone':
            validators = [self.phone_validator]
        elif self.field_type == 'date':
            validators = [self.date_validator]
        else:
            validators = []

        for validator in validators:
            validator(self.field_type)

    def __str__(self):
        return self.name_field

class FormTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    field_name_1 = models.ForeignKey(FormData, related_name='field_1', on_delete=models.CASCADE)
    field_name_2 = models.ForeignKey(FormData, related_name='field_2', on_delete=models.CASCADE, blank=True, null=True)
    field_name_3 = models.ForeignKey(FormData, related_name='field_3', on_delete=models.CASCADE, blank=True, null=True)
    field_name_4 = models.ForeignKey(FormData, related_name='field_4', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

