from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
class UserAccountManager(BaseUserManager):

    def create_user(self, email,username=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email,username,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(('Please assign is_staff=True for superuser'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(('Please assign is_superuser=True for superuser'))
        return self.create_user(email,username,password,**other_fields)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$',message='phone must be an egyptian phone number...')
    username = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    age = models.IntegerField(null=False)
    password = models.CharField(null=False, max_length=300)
    phone =  models.CharField(null=False,validators=[phone_regex],max_length=14)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name','gender','age','password','phone']
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email