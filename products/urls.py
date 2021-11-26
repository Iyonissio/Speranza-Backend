from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('form', views.create_form, name='form-1'),
    path('viatura', views.carro, name='form-viaturas'),
    path('chapa', views.chapa, name='form-chapa')
]