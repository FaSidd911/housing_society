from django.contrib import admin
from django.urls import path ,re_path
from main import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('login', views.login,name='login'),
    path("addSociety", views.addSociety),
    path('society/<str:item_name>/',views.societyMembers, name='item'),
    path('society/<str:item_name>/societyMembers',views.societyMembers, name='item'),
    re_path(r"[^;]*logout", LogoutView.as_view(), name="logout"),
    path('selectChargesFields',views.selectChargesFields),
    path('addDefaultCharges',views.addDefaultCharges),
    path('homeAfterLogin',views.homeAfterLogin),
    path("editSociety/<str:name>/", views.editSociety, name='editSociety'),
    path("editSociety/<str:name>/editSociety", views.editSociety, name='editSociety'),
    path("deleteSociety/<str:name>/", views.deleteSociety, name='deleteSociety'),
    path("editMemberDetails/<str:name>/<str:memberName>/", views.editMemberDetails, name='editMemberDetails'),
    path("editMemberDetails/<str:name>/<str:memberName>/editMemberDetails", views.editMemberDetails, name='editMemberDetails'),
    path("deleteMember/<str:name>/<str:memberName>", views.deleteMember, name='deleteMember'),  
    path('editMemberDetails/<str:name>/<str:memberName>/editSociety',views.editMemberDetails,name='editMemberDetails'),
    path('editMemberDetails/<str:name>/<str:memberName>/societyMembers',views.editMemberDetails,name='editMemberDetails'),
    path('society/<str:name>/uploadMemberDetails',views.uploadMemberDetails, name='item'),
    
]
