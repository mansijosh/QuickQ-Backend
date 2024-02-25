# apii/urls.py

from django.urls import path
from .views import  get_all_forms,edit_form

urlpatterns = [
    #path('forms/<int:form_id>/', get_forms, name='get_forms'),
    path('get_all_forms/', get_all_forms, name='get_all_forms'),
    path('edit_form/', edit_form, name='edit_form')
    
]   
