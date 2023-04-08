from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    password=models.CharField(max_length=200)

    is_staff = models.BooleanField(default=False, verbose_name='Staff account is activated')
    is_active = models.BooleanField(default=True, verbose_name='account is activated')
    is_admin = models.BooleanField(default=False, verbose_name='staff account')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()


class RAM(models.Model):
    used_memory = models.PositiveIntegerField(default=69)
    total_memory = models.PositiveIntegerField(default=69)
    used_swap = models.PositiveIntegerField(default=69)
    total_swap =models.PositiveIntegerField(default=69) 

    def __str__(self):
        return self.total_memory