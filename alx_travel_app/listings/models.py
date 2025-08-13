from django.db import models

class Payment(models.Model):
    booking_reference = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=50, default="Pending")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255)
