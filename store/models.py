from datetime import datetime
from random import random, randint

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name=_('name'))
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.slug


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True)
    slug = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='productImage')
    in_stock = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'products'
        ordering = ['-createdTime']

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.in_stock = False
        else:
            self.in_stock = True
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Discount(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=225, unique=True)
    amount = models.PositiveIntegerField(help_text='per cent',
                                         validators=[MinValueValidator(1), MaxValueValidator(100)])
    state = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    expired_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}--{self.amount}%'


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    staff_code = models.PositiveIntegerField(default=0, unique=True)

    def save(self, *args, **kwargs):
        self.staff_code = int(f'{datetime.now().year}{datetime.now().month}{datetime.now().day}{randint(1000, 9999)}')
        self.user.is_staff = True
        super(Staff, self).save(*args, **kwargs)
