from django.contrib import admin
from .models import SocietyList,MembersList,DefaultChargesList

admin.site.register(SocietyList)
admin.site.register(DefaultChargesList)
admin.site.register(MembersList)

