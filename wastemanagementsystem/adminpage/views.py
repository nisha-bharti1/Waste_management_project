from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

# Create your views here.
from django.http import HttpResponse

def adminpage(request):
    return render(request,"adminpage/adminhome.html")

def productscoin(request):
    return render(request,"adminpage/productscoin.html")

def productsprice(request):
    return render(request,"adminpage/productsprice.html")

def registereduser(request):
    return render(request,"adminpage/registereduser.html")

def registeredcompany(request):
    return render(request,"adminpage/registeredcompany.html")

def adminlogin(request):
    if request.method == "POST":
        username=request.POST['adminname']
        password=request.POST['adminpassword']
        try:
            user=admin.objects.get(username=username)
        except:
            print('user not found')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('adminpage')
        else:
            print('username and password incorrect')
    return render(request,"adminpage/adminlogin.html")

def adminlogout(request):
    logout(request)
    return redirect('Home')

def adminregister(request):
    return render(request,"adminpage/adminregister.html")