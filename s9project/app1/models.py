from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

# Create your models here.
class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(13)], max_length=13)
    #user = models.OneToOneField(user, on_delete=models.CASCADE)
    #user=models.CharField(max_length=20,default='', null=False)
    #pswd = models.CharField(max_length=20, default='', null=False)

class Area(models.Model):
    pincode = models.CharField(validators = [MinLengthValidator(6), MaxLengthValidator(6)],max_length = 6,unique=True)
    city = models.CharField(max_length = 20)