from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'form_list', views.FormTemplateViewsSet)
router.register(r'form_data', views.FormDataViewsSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_form/', views.GetFormView.as_view()),
]
