from datetime import datetime, time
from random import random, randint

from django.contrib.auth import get_user_model
from django.db import models

from store.models import Product

User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.PositiveSmallIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.customer_id = int(f'{datetime.now().year}{datetime.now().month}{datetime.now().day}{randint(1000, 9999)}')
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user}'


class Like(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} has been liked by {self.customer}'
