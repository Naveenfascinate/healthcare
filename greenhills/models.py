from datetime import datetime
from django.db import models


# Create your models here.
class UserPayments(models.Model):
    email = models.EmailField()
    subscription = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    price_paid = models.FloatField()
    paid_date = models.DateField()
    expiry_date = models.DateField()
    expired = models.BooleanField(default=False)

