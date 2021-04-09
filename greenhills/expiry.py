import time
from datetime import date
from .models import UserPayments


def expired_check():
    today = date.today()
    payments = UserPayments.objects.filter(expired=False)
    for user in payments:
        if today > user.expiry_date:
            user.expired = True
            user.save()
