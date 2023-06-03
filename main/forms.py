# authentication/forms.py
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-lg'}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
    
    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Field('username', css_class='form-control-lg'),
    #         Field('password', css_class='form-control-lg')
    #     )
    


    
class Meta:
    model = User
    fields = ["username", "first_name"]
    
    

class ChargesForm(forms.Form):
    elcty = forms.CharField(label='elcty', required=False)
    wtrbll = forms.CharField(label='wtrbll', required=False)
    prkng = forms.CharField(label='prkng', required=False)
    mncpl = forms.CharField(label='mncpl', required=False)
    snkng = forms.CharField(label='snkng', required=False)
    nccpncy = forms.CharField(label='nccpncy', required=False)
    pnlty = forms.CharField(label='pnlty', required=False)
    
class MembersForm(forms.Form):
    memberName = forms.CharField(label='memberName')
    flatno = forms.CharField(label='flatno')
    openingBalance = forms.CharField(label='openingBalance')
    closingBalance = forms.CharField(label='closingBalance')
    elcty = forms.CharField(label='elcty', required=False)
    wtrbll = forms.CharField(label='wtrbll', required=False)
    prkng = forms.CharField(label='prkng', required=False)
    mncpl = forms.CharField(label='mncpl', required=False)
    snkng = forms.CharField(label='snkng', required=False)
    nccpncy = forms.CharField(label='nccpncy', required=False)
    pnlty = forms.CharField(label='pnlty', required=False)
    
    def __init__(self, *args, **kwargs):
        super(MembersForm, self).__init__(*args, **kwargs)
        self.fields['elcty'].initial = '0'
    