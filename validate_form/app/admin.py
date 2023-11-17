from django.contrib import admin
from . import models


@admin.register(models.FormTemplate)
class FormTemplateAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']


@admin.register(models.FormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
