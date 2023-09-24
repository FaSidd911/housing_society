from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db import models


class SocietyList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    societyName = models.CharField(max_length=500)
    regno = models.CharField(max_length=122)
    ctsno = models.CharField(max_length=122)
    panno = models.CharField(max_length=122)
    gstno = models.CharField(max_length=122)
    address = models.TextField()
    status = models.CharField(max_length=122, default="Active")
    date_add_society = models.DateField()

    def __str__(self):
        return self.societyName
    
class MembersList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    memberSocietyName = models.ForeignKey(SocietyList,on_delete=models.CASCADE)
    Member_Name = models.CharField(max_length=500)
    Flat_No = models.CharField(max_length=122) 
    building = models.CharField(max_length=122)
    wing = models.CharField(max_length=122)
    Contact_Number = models.CharField(max_length=122)
    Balance = models.CharField(max_length=122)
    PAN_Number = models.CharField(max_length=122)
    Aadhar_Number = models.CharField(max_length=122)
    date_add_member = models.DateField()

    def __str__(self):
        return self.Member_Name
    
    
class DefaultChargesList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    chargesSocietyName = models.ForeignKey(SocietyList,on_delete=models.CASCADE)
    Water_Charges = models.CharField(max_length=122)
    Municipal_Tax = models.CharField(max_length=122)
    Maintainance_Charges = models.CharField(max_length=122)
    Interest_from_Bank_Savings_Account = models.CharField(max_length=122)
    Membership_Subscription_Charges = models.CharField(max_length=122)
    Audit_Fees = models.CharField(max_length=122)
    Staff_Welfare = models.CharField(max_length=122)
    Accounting_Charges = models.CharField(max_length=122)
    Postage_Courier_Charges = models.CharField(max_length=122)
    Repair_Maintainence_Electrical = models.CharField(max_length=122)
    Depreciation = models.CharField(max_length=122)
    Meeting_Expenses = models.CharField(max_length=122)
    Telephone_Charges = models.CharField(max_length=122)
    Electricity_Charges = models.CharField(max_length=122)
    Security_Charges = models.CharField(max_length=122)
    Printing_Stationary = models.CharField(max_length=122)
    Repair_Maintainence = models.CharField(max_length=122)
    Conveyance = models.CharField(max_length=122)
    Gardening_Expenses = models.CharField(max_length=122)
    Bank_Charges = models.CharField(max_length=122)
    Plumbing_Expenses = models.CharField(max_length=122)
    Salary_to_Staff = models.CharField(max_length=122)
    Service_Charges = models.CharField(max_length=122)
    Sinking_Funds = models.CharField(max_length=122)
    Repair_Funds = models.CharField(max_length=122)
    Parking_Charges = models.CharField(max_length=122)
    Property_Tax = models.CharField(max_length=122)
    Miscellaneous_Charges = models.CharField(max_length=122)
    Water_Charges_Paid  = models.CharField(max_length=122)
    
    def __str__(self):
        return self.chargesSocietyName.societyName 
    
class MemberChargesList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    chargesSocietyName = models.ForeignKey(SocietyList,on_delete=models.CASCADE)
    chargesMemberName = models.ForeignKey(MembersList,on_delete=models.CASCADE)
    Flat_No = models.CharField(max_length=122) 
    building = models.CharField(max_length=122)
    wing = models.CharField(max_length=122)
    Water_Charges = models.CharField(max_length=122)
    Municipal_Tax = models.CharField(max_length=122)
    Maintainance_Charges = models.CharField(max_length=122)
    Interest_from_Bank_Savings_Account = models.CharField(max_length=122)
    Membership_Subscription_Charges = models.CharField(max_length=122)
    Audit_Fees = models.CharField(max_length=122)
    Staff_Welfare = models.CharField(max_length=122)
    Accounting_Charges = models.CharField(max_length=122)
    Postage_Courier_Charges = models.CharField(max_length=122)
    Repair_Maintainence_Electrical = models.CharField(max_length=122)
    Depreciation = models.CharField(max_length=122)
    Meeting_Expenses = models.CharField(max_length=122)
    Telephone_Charges = models.CharField(max_length=122)
    Electricity_Charges = models.CharField(max_length=122)
    Security_Charges = models.CharField(max_length=122)
    Printing_Stationary = models.CharField(max_length=122)
    Repair_Maintainence = models.CharField(max_length=122)
    Conveyance = models.CharField(max_length=122)
    Gardening_Expenses = models.CharField(max_length=122)
    Bank_Charges = models.CharField(max_length=122)
    Plumbing_Expenses = models.CharField(max_length=122)
    Salary_to_Staff = models.CharField(max_length=122)
    Service_Charges = models.CharField(max_length=122)
    Sinking_Funds = models.CharField(max_length=122)
    Repair_Funds = models.CharField(max_length=122)
    Parking_Charges = models.CharField(max_length=122)
    Property_Tax = models.CharField(max_length=122)
    Miscellaneous_Charges = models.CharField(max_length=122)
    Water_Charges_Paid  = models.CharField(max_length=122)
    
    def __str__(self):
        return self.chargesMemberName.Member_Name  + '_' +  self.chargesMemberName.building + '_' +  self.chargesMemberName.Flat_No + '_' +  self.chargesMemberName.wing
    
    
class MonthlyMemberChargesList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    MonthlychargesSocietyName = models.ForeignKey(SocietyList,on_delete=models.CASCADE)
    MonthlychargesMemberName = models.ForeignKey(MembersList,on_delete=models.CASCADE)
    Flat_No = models.CharField(max_length=122) 
    building = models.CharField(max_length=122)
    wing = models.CharField(max_length=122)
    Water_Charges = models.CharField(max_length=122)
    Municipal_Tax = models.CharField(max_length=122)
    Maintainance_Charges = models.CharField(max_length=122)
    Interest_from_Bank_Savings_Account = models.CharField(max_length=122)
    Membership_Subscription_Charges = models.CharField(max_length=122)
    Audit_Fees = models.CharField(max_length=122)
    Staff_Welfare = models.CharField(max_length=122)
    Accounting_Charges = models.CharField(max_length=122)
    Postage_Courier_Charges = models.CharField(max_length=122)
    Repair_Maintainence_Electrical = models.CharField(max_length=122)
    Depreciation = models.CharField(max_length=122)
    Meeting_Expenses = models.CharField(max_length=122)
    Telephone_Charges = models.CharField(max_length=122)
    Electricity_Charges = models.CharField(max_length=122)
    Security_Charges = models.CharField(max_length=122)
    Printing_Stationary = models.CharField(max_length=122)
    Repair_Maintainence = models.CharField(max_length=122)
    Conveyance = models.CharField(max_length=122)
    Gardening_Expenses = models.CharField(max_length=122)
    Bank_Charges = models.CharField(max_length=122)
    Plumbing_Expenses = models.CharField(max_length=122)
    Salary_to_Staff = models.CharField(max_length=122)
    Service_Charges = models.CharField(max_length=122)
    Sinking_Funds = models.CharField(max_length=122)
    Repair_Funds = models.CharField(max_length=122)
    Parking_Charges = models.CharField(max_length=122)
    Property_Tax = models.CharField(max_length=122)
    Miscellaneous_Charges = models.CharField(max_length=122)
    Water_Charges_Paid  = models.CharField(max_length=122)
    Current_Month_Total = models.CharField(max_length=122)
    Arrears = models.CharField(max_length=122)
    Total = models.CharField(max_length=122)
    date_monthly_charges = models.DateField()
    
    def __str__(self):
        return self.MonthlychargesMemberName.Member_Name  + '_' +  self.MonthlychargesMemberName.building + '_' +  self.MonthlychargesMemberName.Flat_No + '_' +  self.MonthlychargesMemberName.wing