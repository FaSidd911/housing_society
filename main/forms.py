# authentication/forms.py
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-lg'}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class Meta:
    model = User
    fields = ["username", "first_name"]
    
    



