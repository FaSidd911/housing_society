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
    path('upload_doc/<str:name>/',views.upload_doc, name="upload_doc"),
    path('upload_doc/<str:name>/upload_doc',views.upload_doc, name="upload_doc"),
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
    path('show_member_detail/<str:name>/',views.show_member_detail, name='show_member_detail'),
    path("deleteSociety/<str:memberSocietyName>/<str:building>/<str:FlatNo>/<str:wing>", views.deleteMember, name='deleteMember'),
    path("editMember/<str:memberSocietyName>/<str:building>/<str:FlatNo>/<str:wing>", views.editMember, name='editMember'),
    path("update_member", views.update_member, name='update_member'),
    path("import_members", views.import_members, name='import_members'),
    path("import_members/<str:name>/", views.import_members, name='import_members'),
    path("import_members/<str:name>/import_members", views.import_members, name='import_members'),
    path("download_file/<str:name>/", views.download_file, name='download_file'),
    path("download_doc/<str:name>/<str:doc>/", views.download_doc, name='download_doc'),
    path('show_member_detail', views.show_member_detail),
    path('charges_detail/<str:name>/<str:mnth>', views.charges_detail, name='charges_detail'), 
    path('charges_value_edit/<str:name>/<str:mem_bldng>/<str:mem_flat>/<str:mem_wing>/<str:mnth>', views.charges_value_edit, name='charges_value_edit'), 
    path('charges_value_edit_submit/<str:name>/<str:mem_bldng>/<str:mem_flat>/<str:mem_wing>', views.charges_value_edit_submit, name='charges_value_edit_submit'), 
    path('generate_charges/<str:name>', views.generate_charges, name='generate_charges'), 
    path('generate_bill/<str:name>/<str:mnth>', views.generate_bill, name='generate_bill'), 
    path('view_member_bill/<str:name>/<str:mem_bldng>/<str:mem_flat>/<str:mem_wing>/<str:mnth>', views.view_member_bill, name='view_member_bill'), 
    path('receipt_template/<str:name>/<str:mem_bldng>/<str:mem_flat>/<str:mem_wing>/<str:mnth>', views.receipt_template, name='receipt_template'), 
    path('bill_to_pdf/<str:name>/<str:mem_bldng>/<str:mem_flat>/<str:mem_wing>/<str:mnth>', views.bill_to_pdf ,name='bill_to_pdf'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
