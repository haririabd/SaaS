from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_test, name='testmain'),
    path('contact-form/', views.contact_form, name='contact_form'),
    path('contact-form-only/', views.contact_form_only, name='contact_form_only'),
]