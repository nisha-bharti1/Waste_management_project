from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage(request):
    return render(request,"wmsHome.html")

def contact(request):
    return HttpResponse("I am at contact us page")