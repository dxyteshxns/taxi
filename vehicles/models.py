from django.db import models
from django.conf import settings

class Vehicle(models.Model):
    driver = models.ForeignKey('drivers.DriverProfile', on_delete=models.CASCADE, related_name='vehicles')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    plate_number = models.CharField(max_length=20)
    description = models.TextField(blank=True)

