from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class RAM(models.Model):
    used_memory = models.PositiveIntegerField(default=69)
    total_memory = models.PositiveIntegerField(default=69)
    used_swap = models.PositiveIntegerField(default=69)
    total_swap =models.PositiveIntegerField(default=69) 

    def __str__(self):
        return self.total_memory