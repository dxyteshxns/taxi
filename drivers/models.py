from django.db import models
from django.conf import settings

class DriverProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    license_number = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=(('online','Online'),('offline','Offline')), default='offline')

