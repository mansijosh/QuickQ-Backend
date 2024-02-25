# models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    # Add more user fields as needed

class Form(models.Model):
    form_name = models.CharField(max_length=255)
    questions = models.JSONField()
    # Add more form fields as needed

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    responses = models.JSONField()
    # Add more response fields as needed
