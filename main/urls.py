from django.contrib import admin
from django.urls import path ,re_path
from main import views 
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

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
    
    #---------------------------------------------------------------------------------------------------
    
    path("society_detail", views.society_detail,name="society_detail"),
    path('add_new_society',views.add_new_society),
    path('upload_doc',views.upload_doc, name="upload_doc"),
    path('upload_doc_temp',views.upload_doc_temp, name="upload_doc_temp"),
    path('upload_doc_temp/<str:name>',views.upload_doc_temp, name="upload_doc_temp"),
    path('add_charges', views.add_charges),
    path('add_value', views.add_value),
    path('persist_society_details', views.persist_society_details),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
