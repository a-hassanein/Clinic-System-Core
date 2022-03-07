from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Doctor(AbstractUser):
    phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$',message='phone must be an egyptian phone number...')
    username = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    age = models.IntegerField(null=False)
    password = models.CharField(null=False, max_length=300)
    phone =  models.CharField(null=False,validators=[phone_regex],max_length=14)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name','gender','age','password','phone']