from django.db import models

class Payment(models.Model):
    trip = models.OneToOneField('trips.Trip', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=(('pending','Pending'),('paid','Paid'),('failed','Failed')))
    transaction_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

