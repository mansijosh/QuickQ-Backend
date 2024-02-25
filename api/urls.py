# urls.py
from django.urls import path
from .views import create_form, add_responses, delete_form
#from .views import IndexView

urlpatterns = [
    #path('', IndexView.as_view(), name='index'),
    path('create_form/', create_form, name='create_form'),
    path('add_responses/', add_responses, name='add_responses'),
    path('delete_form/<str:form_id>/', delete_form, name='delete_form'),
    # path('add_responses/', add_responses, name='add_responses'),
    # Add more URLs as needed
]
