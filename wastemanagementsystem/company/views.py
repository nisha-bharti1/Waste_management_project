from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

# Create your views here.
from django.http import HttpResponse

def companypage(request):
    return render(request,"company/companyhome.html")

def saleproducts(request):
    return render(request,"company/saleproducts.html")

def salehistory(request):
    return render(request,"company/salehistory.html")

def purchaseraw(request):
    return render(request,"company/purchaseraw.html")

def purchasehistory(request):
    return render(request,"company/purchasehistory.html")

def companylogin(request):
    if request.method == "POST":
        username=request.POST['companyname']
        password=request.POST['companypassword']
        try:
            user=company.objects.get(username=username)
        except:
            print('user not found')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('companypage')
        else:
            print('username and password incorrect')
    return render(request,"company/companylogin.html")

def companyregister(request):
    return render(request,"company/companyregister.html")


def companylogout(request):
    logout(request)
    return redirect('Home')
