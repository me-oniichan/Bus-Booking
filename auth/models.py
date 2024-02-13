from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from .utils import password_validation, username_validation

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password, email, display_name=''):
        email = self.normalize_email(email)
        password_validation(password)
        
        user: Users = self.model(username=username, display_name=display_name, email=email)
        user.set_password(password)
        user.full_clean()
        user.save() 
        return user

class Users(AbstractUser):
    last_name = None
    first_name = None
    username = models.CharField(unique=True, max_length=25, validators=[username_validation])
    display_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, validators=[validate_email])

    objects = UserManager()
