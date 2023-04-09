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
    mac_id = models.PositiveIntegerField(primary_key = True,default=0) #it is actually the id of user
    kernel_version= models.CharField(max_length=25)
    host_name= models.CharField(max_length=50)
    name = models.CharField(max_length=20,default="ubuntu")
    os_version= models.CharField(max_length=25)
    cpu_count = models.PositiveIntegerField(blank=True)
    cpus = models.JSONField(default=None, blank=True, null=True)
    temp = models.JSONField(default=None, blank=True, null=True)

class RAM(models.Model):
    sys_id = models.ForeignKey(SysInfo, on_delete=models.CASCADE, default=0)
    used_memory = models.PositiveIntegerField(default=69)
    total_memory = models.PositiveIntegerField(default=69)
    used_swap = models.PositiveIntegerField(default=69)
    total_swap =models.PositiveIntegerField(default=69)

    def _str_(self):
        return str(self.sys_id)
    
class Process(models.Model):
    sys_id = models.ForeignKey(SysInfo, on_delete=models.CASCADE,default=0)
    pid = models.CharField(max_length=69)
    name = models.CharField(max_length=69)
    written_bytes = models.PositiveIntegerField(default=0)
    total_written_bytes = models.PositiveIntegerField(default=0)
    read_bytes = models.PositiveIntegerField(default=0)
    total_read_bytes = models.PositiveIntegerField(default=0)

    def _str_(self):
        return str(self.p_id)