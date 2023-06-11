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
    
       
class MembersForm(forms.Form):
    Member_Name = forms.CharField(label='Member_Name')
    Flat_No = forms.CharField(label='Flat_No')
    Opening_Balance = forms.IntegerField(label='Opening_Balance')
    Closing_Balance = forms.IntegerField(label='Closing_Balance')
    Electricity_Charges = forms.CharField(label='Electricity_Charges', required=False)
    Municipal_Tax = forms.CharField(label='Municipal_Tax', required=False)
    Water_Charges = forms.CharField(label='Water_Charges', required=False)
    Maintainance_Charges = forms.CharField(label='Maintainance_Charges', required=False)
    Service_Charges = forms.CharField(label='Service_Charges', required=False)
    Sinking_Fund = forms.CharField(label='Sinking_Fund', required=False)
    Repair_Fund = forms.CharField(label='Repair_Fund', required=False)
    
    def __init__(self, *args, **kwargs):
        super(MembersForm, self).__init__(*args, **kwargs)
        self.fields['Electricity_Charges'].initial = '0'
        

class ChargesForm(forms.Form):
    Electricity_Charges = forms.CharField(label='Electricity_Charges', required=False)
    Municipal_Tax = forms.CharField(label='Municipal_Tax', required=False)
    Water_Charges = forms.CharField(label='Water_Charges', required=False)
    Maintainance_Charges = forms.CharField(label='Maintainance_Charges', required=False)
    Service_Charges = forms.CharField(label='Service_Charges', required=False)
    Sinking_Fund = forms.CharField(label='Sinking_Fund', required=False)
    Repair_Fund = forms.CharField(label='Repair_Fund', required=False)   

class EditSocietyForm(forms.Form):
    Society_Name = forms.CharField(label='Society_Name')
    Reg_No = forms.CharField(label='Reg_No')
    Address = forms.CharField(label='Address')
    
    
class EditMembersForm(forms.Form):
    Member_Name = forms.CharField(label='Member_Name')
    Flat_No = forms.CharField(label='Flat_No')
    Opening_Balance = forms.IntegerField(label='Opening_Balance')
    Closing_Balance = forms.IntegerField(label='Closing_Balance')
    Electricity_Charges = forms.CharField(label='Electricity_Charges', required=False)
    Municipal_Tax = forms.CharField(label='Municipal_Tax', required=False)
    Water_Charges = forms.CharField(label='Water_Charges', required=False)
    Maintainance_Charges = forms.CharField(label='Maintainance_Charges', required=False)
    Service_Charges = forms.CharField(label='Service_Charges', required=False)
    Sinking_Fund = forms.CharField(label='Sinking_Fund', required=False)
    Repair_Fund = forms.CharField(label='Repair_Fund', required=False)