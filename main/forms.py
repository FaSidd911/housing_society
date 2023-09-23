# authentication/forms.py
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class LoginForm(forms.Form):
    # username = forms.CharField(widget=forms.Textarea)
    # password = forms.CharField(max_length=63, widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = ["username"]
        # widget=forms.Input(attrs={'class': 'form-control-lg; width: 200px ;height: 50px'})
    



