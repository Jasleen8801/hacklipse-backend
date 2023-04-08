from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin

from .managers import CustomUserManager
from jsonfield import JSONField
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

    def __str__(self):
       return str(self.email)

#one user can have multiple devices

class SysInfo(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    kernel_version= models.CharField(max_length=25)
    host_name= models.CharField(max_length=50)
    os_version= models.CharField(max_length=25)
    cpu_count = models.PositiveIntegerField()
    cpus = models.JSONField()
    temp = models.JSONField()

class RAM(models.Model):
    sys_id = models.ForeignKey(SysInfo, on_delete = models.CASCADE,default=69)
    used_memory = models.PositiveIntegerField(default=69)
    total_memory = models.PositiveIntegerField(default=69)
    used_swap = models.PositiveIntegerField(default=69)
    total_swap =models.PositiveIntegerField(default=69) 

    def __str__(self):
        return str(self.sys_id)
    
class Process(models.Model):
    sys_id = models.ForeignKey(SysInfo, on_delete = models.CASCADE,default=69)
    process_name = models.CharField(max_length=69)
    disk_usage = models.CharField(max_length=69)

