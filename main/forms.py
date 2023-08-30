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
    Water_Charges = forms.CharField(label='Water_Charges')
    Municipal_Tax = forms.CharField(label='Municipal_Tax')
    Maintainance_Charges = forms.CharField(label='Maintainance_Charges')
    Interest_from_Bank_Savings_Account = forms.CharField(label='Interest_from_Bank_Savings_Account')
    Membership_Subscription_Charges = forms.CharField(label='Membership_&_Subscription_Charges')
    Audit_Fees = forms.CharField(label='Audit_Fees')
    Staff_Welfare = forms.CharField(label='Staff_Welfare')
    Accounting_Charges = forms.CharField(label='Accounting_Charges')
    Postage_Courier_Charges = forms.CharField(label='Postage_&_Courier_Charges')
    Repair_Maintainence_Electrical = forms.CharField(label='Repair_Maintainence_Electrical')
    Depreciation = forms.CharField(label='Depreciation')
    Meeting_Expenses = forms.CharField(label='Meeting_Expenses')
    Telephone_Charges = forms.CharField(label='Telephone_Charges')
    Electricity_Charges = forms.CharField(label='Electricity_Charges')
    Security_Charges = forms.CharField(label='Security_Charges')
    Printing_Stationary = forms.CharField(label='Printing_&_Stationary')
    Repair_Maintainence = forms.CharField(label='Repair_&_Maintainence')
    Conveyance = forms.CharField(label='Conveyance')
    Gardening_Expenses = forms.CharField(label='Gardening_Expenses')
    Bank_Charges = forms.CharField(label='Bank_Charges')
    Plumbing_Expenses = forms.CharField(label='Plumbing_Expenses')
    Salary_to_Staff = forms.CharField(label='Salary_to_Staff')
    Service_Charges = forms.CharField(label='Service_Charges')
    Sinking_Funds = forms.CharField(label='Sinking_Funds')
    Repair_Funds = forms.CharField(label='Repair_Funds')
    Parking_Charges = forms.CharField(label='Parking_Charges')
    Property_Tax = forms.CharField(label='Property_Tax')
    Miscellaneous_Charges = forms.CharField(label='Miscellaneous_Charges')
    Water_Charges_Paid  = forms.CharField(label='Water_Charges_Paid')

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