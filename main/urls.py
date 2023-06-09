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
]
