from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path('',views.adminpage,name="adminpage"),
    path('productscoin',views.productscoin,name="productscoin"),
    path('productsprice',views.productsprice,name="productsprice"),
    path('registereduser',views.registereduser,name="registereduser"),
    path('registeredcompany',views.registeredcompany,name="registeredcompany"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('adminlogout',views.adminlogout,name="adminlogout"),
    path('adminregister',views.adminregister,name="adminregister"),

]