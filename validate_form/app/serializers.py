from rest_framework import serializers
from .validators import validate_email, validate_phone, validate_date
from . import models


class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FormData
        fields = '__all__'

    def validate(self, data):
        field_type = data.get('field_type')
        value = data.get('value')

        if field_type == 'email':
            validate_email(value)
        elif field_type == 'phone':
            validate_phone(value)
        elif field_type == 'date':
            validate_date(value)

        return data


class FormTemplateSerializer(serializers.ModelSerializer):
    field_name_1 = FormDataSerializer()
    field_name_2 = FormDataSerializer()
    field_name_3 = FormDataSerializer()
    field_name_4 = FormDataSerializer()

    class Meta:
        model = models.FormTemplate
        fields = ('name', 'field_name_1', 'field_name_2', 'field_name_3', 'field_name_4')

    def create(self, validated_data):
        field_name_1_data = validated_data.pop('field_name_1')
        field_name_2_data = validated_data.pop('field_name_2')
        field_name_3_data = validated_data.pop('field_name_3')
        field_name_4_data = validated_data.pop('field_name_4')

        field_name_1 = models.FormData.objects.create(**field_name_1_data)
        field_name_2 = models.FormData.objects.create(**field_name_2_data)
        field_name_3 = models.FormData.objects.create(**field_name_3_data)
        field_name_4 = models.FormData.objects.create(**field_name_4_data)

        form_template = models.FormTemplate.objects.create(
            field_name_1=field_name_1,
            field_name_2=field_name_2,
            field_name_3=field_name_3,
            field_name_4=field_name_4,
            **validated_data
        )

        return form_template






