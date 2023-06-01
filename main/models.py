from django.db import models

# Create your models here.
from django.db import models


class SocietyList(models.Model):
    societyName = models.CharField(max_length=122,  unique=True)
    regno = models.CharField(max_length=122)
    address = models.TextField()
    date_add_society = models.DateField()
    user = models.CharField(max_length=122, blank=True, null=True)
    charges_fields=models.CharField(max_length=122, blank=True, null=True)

    def __str__(self):
        return self.societyName
    
class MembersList(models.Model):
    user = models.CharField(max_length=122,blank=True, null=True)
    societyName = models.CharField(max_length=122)
    memberName = models.CharField(max_length=122,  unique=True)
    flatno = models.CharField(max_length=122)
    openingBalance = models.IntegerField()
    closingBalance = models.IntegerField()  
    elcty = models.CharField(max_length=122,blank=True, null=True)
    wtrbll = models.CharField(max_length=122,blank=True, null=True)
    prkng = models.CharField(max_length=122,blank=True, null=True)
    mncpl = models.CharField(max_length=122,blank=True, null=True)
    snkng = models.CharField(max_length=122,blank=True, null=True)
    nccpncy = models.CharField(max_length=122,blank=True, null=True)
    pnlty = models.CharField(max_length=122,blank=True, null=True)
    date_add_member = models.DateField()

    def __str__(self):
        return self.memberName
    
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
#         return self.memberName