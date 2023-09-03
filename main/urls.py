from django.contrib import admin
from django.urls import path ,re_path
from main import views 
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    re_path(r"[^;]*logout", LogoutView.as_view(), name="logout"),
    path('', views.index),
    path('index', views.index),
    path('login', views.login,name='login'),
    path("society_detail", views.society_detail,name="society_detail"),
    path('add_new_society',views.add_new_society),
    path('upload_doc',views.upload_doc, name="upload_doc"),
    path('upload_doc_temp',views.upload_doc_temp, name="upload_doc_temp"),
    path('upload_doc_temp/<str:name>',views.upload_doc_temp, name="upload_doc_temp"),
    path('add_charges', views.add_charges),
    path('add_value', views.add_value),
    path('persist_society_details', views.persist_society_details),
    path("deleteSociety/<str:name>/", views.deleteSociety, name='deleteSociety'),
    path("edit_scoiety/<str:name>/", views.edit_society, name='edit_society'),
    path("edit_scoiety/<str:name>/save_edit_society", views.save_edit_society, name='save_edit_society'),
    path("edit_charges/<str:name>/", views.edit_charges, name='edit_charges'),
    path("edit_charges/<str:name>/edit_value", views.edit_value, name='edit_value'),
    path("edit_charges/<str:name>/edit_society_values", views.edit_society_values, name='edit_society_values'),
    path('add_member/<str:name>/',views.add_member,name = 'add_member'),
    path('add_member/<str:name>/add_member',views.add_member,name = 'add_member'),
    path('member_detail/<str:name>/',views.member_detail, name='member_detail'),
    path("deleteSociety/<str:memberSocietyName>/<str:building>/<str:FlatNo>", views.deleteMember, name='deleteMember'),
    path("editMember/<str:memberSocietyName>/<str:building>/<str:FlatNo>", views.editMember, name='editMember'),
    path("update_member", views.update_member, name='update_member'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
