from django.urls import path
from . import views
urlpatterns = [
        path('', views.mainhome,name='mainhome'),
        path('login/',views.login,name='login'),
        path('feedback/',views.feedback,name='feedback'),
        path('forgot/',views.forgot,name='forgot'),
        path('error/',views.error,name='error'),
        path('home/',views.home,name='home'),
        path('contact/',views.contact,name='contact'),
        path('cardetail/',views.cardetail,name='cardetail'),
        path('booking/',views.booking,name='booking'),
        path('about/',views.about,name='about'),
        path('mainhome/', views.mainhome,name='mainhome'),
        path("getres/",views.getres,name="getres"),
        path('checkuser/',views.checkuser,name="checkuser"),
        path('getdetails/',views.getdetails,name="getdetails"),
        path('getcontact/',views.getcontact,name="getcontact"),
        path('email/',views.email,name="email"),
        path('getfeedback/',views.getfeedback,name="getfeedback"),
        path('update/',views.update,name="update"),

  ]
