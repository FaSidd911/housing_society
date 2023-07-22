from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db import models


class SocietyList(models.Model):
    society_id = models.AutoField( primary_key = True, editable = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    societyName = models.CharField(max_length=500)
    regno = models.CharField(max_length=122)
    address = models.TextField()
    date_add_society = models.DateField()
    charges_fields=models.CharField(max_length=122, blank=True, null=True)

    def __str__(self):
        return self.societyName
    
class MembersList(models.Model):
    member_id = models.AutoField( primary_key = True, editable = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    memberSocietyName = models.ForeignKey(SocietyList,on_delete=models.CASCADE)
    Member_Name = models.CharField(max_length=500)
    Flat_No = models.CharField(max_length=122)
    Opening_Balance = models.IntegerField()
    Closing_Balance = models.IntegerField()  
    Electricity_Charges = models.CharField(max_length=122,blank=True, null=True)
    Water_Charges = models.CharField(max_length=122,blank=True, null=True)
    Maintainance_Charges = models.CharField(max_length=122,blank=True, null=True)
    Municipal_Tax = models.CharField(max_length=122,blank=True, null=True)
    Sinking_Fund = models.CharField(max_length=122,blank=True, null=True)
    Repair_Fund = models.CharField(max_length=122,blank=True, null=True)
    Service_Charges = models.CharField(max_length=122,blank=True, null=True)
    date_add_member = models.DateField()

    def __str__(self):
        return self.Member_Name
    
    
# class ChargesList(models.Model):
#     elcty = models.CharField(max_length=122)
#     wtrbll = models.CharField(max_length=122)
#     prkng = models.CharField(max_length=122)
#     mncpl = models.CharField(max_length=122)
#     snkng = models.CharField(max_length=122)
#     nccpncy = models.CharField(max_length=122)
#     pnlty = models.CharField(max_length=122)
#     date_add_member = models.DateField()
#     user = models.CharField(max_length=122,blank=True, null=True)
    
#     def __str__(self):
#         return self.Member_Name