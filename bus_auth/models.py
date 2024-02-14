from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from .utils import password_validation, username_validation

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password, email):
        email = self.normalize_email(email)
        password_validation(password)
        
        user: Users = self.model(username=username, email=email)
        user.set_password(password)
        user.full_clean()
        user.save() 
        return user
    def create_superuser(self, username, password, email):
        user = self.create_user(username, password, email)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class Users(AbstractUser):
    last_name = None
    first_name = None
    username = models.CharField(unique=True, max_length=25, validators=[username_validation])
    email = models.EmailField(unique=True)

    objects = UserManager()
