from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path('',views.companypage,name="companypage"),
    path('saleproducts',views.saleproducts,name='saleproducts'),
    path('salehistory',views.salehistory,name='salehistory'),
    path('purchaseraw',views.purchaseraw,name='purchaseraw'),
    path('purchasehistory',views.purchasehistory,name='purchasehistory'),
    path('companylogin',views.companylogin,name='companylogin'),
    path('companyregister',views.companyregister,name='companyregister'),
    path('companylogout',views.companylogout,name="companylogout"),

]

