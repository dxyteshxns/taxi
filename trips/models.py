from django.db import models
from django.conf import settings

class Trip(models.Model):
    rider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trips')
    driver = models.ForeignKey('drivers.DriverProfile', null=True, blank=True, on_delete=models.SET_NULL)
    vehicle = models.ForeignKey('vehicles.Vehicle', null=True, blank=True, on_delete=models.SET_NULL)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=(('requested','Requested'),('accepted','Accepted'),('ongoing','Ongoing'),('completed','Completed'),('cancelled','Cancelled')), default='requested')
    created_at = models.DateTimeField(auto_now_add=True)
