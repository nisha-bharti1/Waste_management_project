from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path('',views.userspage,name="userpage"),
    path('productsprice',views.productsprice,name="productsprice"),
    path('productscoin',views.productscoin,name="productscoin"),
    path('history',views.history,name="history"),
    path('salescrap',views.salescrap,name="salescrap"),
    path('userregister',views.userregister,name="userregister"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userlogout',views.userlogout,name="userlogout"),

]