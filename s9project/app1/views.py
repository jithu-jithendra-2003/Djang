from django.shortcuts import render
from django.http import HttpResponse
from .models import Details
# Create your views here.
def mainhome(request):
    return render(request,"mainhome.html")
def error(request):
    return render(request,"error.html")
def login(request):
    return render(request,"login.html")
def home(request):
    return render(request,"home.html")
def contact(request):
    return render(request,"contact.html")
def cardetail(request):
    return render(request,"cardetail.html")
def booking(request):
    return render(request,"booking.html")
def about(request):
    return render(request,"about.html")

