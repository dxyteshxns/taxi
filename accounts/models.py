from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    ROLE_CHOICES = (('rider','Rider'), ('driver','Driver'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='rider')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
