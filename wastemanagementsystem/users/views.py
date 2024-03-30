from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product,scrap
from .forms import NewUserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from django.contrib.auth.models import User
# Create your views here.


def userspage(request):
    return render(request,"users/usershome.html")

def productsprice(request):
    products=product.objects.all()
    params={'Products':products}
    return render(request,"users/productprice.html",params)

def productscoin(request):
    products=product.objects.all()
    params={'Products':products}
    return render(request,"users/productcoin.html",params)

def history(request):
    return render(request,"users/history.html")

def salescrap(request):
    scraps=scrap.objects.all()
    params={'scraps':scraps}
    return render(request,"users/salescrap.html",params)

def userregister(request):

    if request.method=="POST":
        email=request.POST['email']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        data=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
        data.save()
        return redirect('userlogin')
    
    return render(request,'users/register.html')


    # if request.method == "POST":
    #     form = NewUserForm(request.POST)
        
    #     if form.is_valid():
    #         user=form.save()
    #         print(user)
    #         login(request,user)
    #         messages.success(request,"Registration successful.")
    #         return redirect("userlogin")
    #     messages.error(request, "Unsuccessful registration. Invalid Information. ")
    # form = NewUserForm() 
    # return render(request=request, template_name="users/register.html", context={"register_form":form})

def userlogin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            print('user not found')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('userpage')
        else:
            print('username and password incorrect')
    return render(request,"users/login.html")

def userlogout(request):
    logout(request)
    return redirect('Home')