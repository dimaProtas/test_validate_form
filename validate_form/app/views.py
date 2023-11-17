from rest_framework import viewsets, views, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .validators import validate_email, validate_phone, validate_date

from . import models
from . import serializers


class FormTemplateViewsSet(viewsets.ModelViewSet):
    queryset = models.FormTemplate.objects.all()
    serializer_class = serializers.FormTemplateSerializer


class FormDataViewsSet(viewsets.ModelViewSet):
    queryset = models.FormData.objects.all()
    serializer_class = serializers.FormDataSerializer


class GetFormView(views.APIView):
    def post(self, request, *args, **kwargs):
        # Шаг 1: Преобразование входных данных в словарь
        form_data = request.data

        # Шаг 2: Поиск соответствующего шаблона формы
        templates = models.FormTemplate.objects.all()

        for template in templates:
            is_match = True

            for i in range(1, 5):  # Перебор всех полей шаблона
                field_name = f'field_name_{i}'

                # Игнорировать пустые поля в шаблоне
                if getattr(template, field_name).name_field == '':
                    continue

                if getattr(template, field_name).name_field not in form_data:
                    is_match = False
                    break

                if getattr(template, field_name).value != form_data[getattr(template, field_name).name_field]:
                    is_match = False
                    break

            # Шаг 3: Если шаблон найден, вернуть его имя
            if is_match:
                serializer = serializers.FormTemplateSerializer(template)
                return Response({'template_name': serializer.data['name']})

        field_types = {}
        for field_name, field_value in form_data.items():
            field_type = get_field_type(field_value)

            # Добавить тип поля в словарь
            field_types[field_name] = field_type

        return Response({'field_types': field_types}, status=status.HTTP_200_OK)

def get_field_type(field_value):
    try:
        # Попытка валидации значения как email
        validate_email(field_value)
        return 'email'
    except ValidationError:
        pass

    try:
        # Попытка валидации значения как номера телефона
        validate_phone(field_value)
        return 'phone'
    except ValidationError:
        pass

    try:
        # Попытка валидации значения как даты
        validate_date(field_value)
        return 'date'
    except ValidationError:
        pass
    # Если ни одна валидация не прошла, возвращаем 'text'
    return 'text'