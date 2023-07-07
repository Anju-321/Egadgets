from typing import Any, Dict
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username",'password1','password2']
class Logform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)