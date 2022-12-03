from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from django.core.mail import send_mail
client=MongoClient("mongodb://127.0.0.1:27017/")

db=client["SDP"]
login=db.stu
booking=db.book
detail=db.det
contact=db.cont
feedback=db.feed
# Create your views here.
def mainhome(request):
    return render(request,"mainhome.html")

def feedback(request):
    return render(request,"feedback.html")
def error(request):
    return render(request,"error.html")
def login(request):
    return render(request,"login.html")

def forgot(request):
    return render(request,"forgot.html")
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

def getres(request):
    if request.method=='POST':
        email=request.POST.get('email')
        user=request.POST.get('user_name')
        passwo=request.POST.get('passwo')
        db.login.insert_one({'email':email,'user':user,'passwo':passwo})
        return render(request,"login.html")
    return render(request,"login.html")

def checkuser(request):
    if request.method=='POST':
        user=request.POST.get('user')
        passwo=request.POST.get('passwo')

        c=db.login.find_one({'user':user})

        if c['user']==user and c['passwo']==passwo:
             return render(request,"home.html")
        else:
            return render(request,"login.html")
    return render(request,"login.html")


def getdetails(request):
    if request.method=='POST':
        pick = request.POST.get('pick')
        drop = request.POST.get('drop')
        date = request.POST.get('date')
        time = request.POST.get('time')
        adult = request.POST.get('adult')
        child = request.POST.get('child')
        car = request.POST.get('car')
        db.booking.insert_one({'pick': pick, 'drop': drop, 'date': date, 'time': time, 'adult': adult, 'child': child, 'car': car})
        Fname=request.POST.get('Fname')
        Lname=request.POST.get('Lname')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        db.detail.insert_one({'Fname':Fname,'Lname':Lname,'email':email,'phno':phno})
        razor = request.POST.get('payment')
        return render(request,"booking.html")
    return render(request,"booking.html")


def getcontact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        issue=request.POST.get('issue')
        location = request.POST.get('location')
        db.contact.insert_one({'name': name, 'issue': issue, 'email': email, 'Location': location})
        return render(request, "home.html")
    return render(request,"home.html")


def getfeedback(request):
    if request.method=='POST':
        star_rating=request.POST.get('star')
        username = request.POST.get('username')
        car = request.POST.get('car')
        feedback=request.POST.get('feedback')
        db.feeback.insert_one({'star_rating':star_rating,'username': username, 'feedback': feedback, 'car': car})
        return render(request, "home.html")
    return render(request,"home.html")

def email(request):
    send_mail(
        'Test Mail Using Django Framework',
        'Hello Sir/Mam'
        'Hope details are correct if not click the link below to re book.\nyutie',
        'nagajithendra.123@gmail.com',
        ['geethu240434@gmail.com'],
        fail_silently = False,
    )