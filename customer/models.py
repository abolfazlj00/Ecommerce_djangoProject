from datetime import datetime, time
from random import random, randint

from django.contrib.auth import get_user_model
from django.db import models

from account.models import CustomUser
from store.models import Discount

User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    customer_id = models.PositiveSmallIntegerField(blank=True, null=True)
    discount_code = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.customer_id = int(f'{datetime.now().year}{datetime.now().month}{datetime.now().day}{randint(1000, 9999)}')
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user}'

