from django.contrib import admin
from .models import SocietyList,MembersList,DefaultChargesList,MemberChargesList,MonthlyMemberChargesList

admin.site.register(SocietyList)
admin.site.register(DefaultChargesList)
admin.site.register(MembersList)
admin.site.register(MemberChargesList)
admin.site.register(MonthlyMemberChargesList)