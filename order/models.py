from django.db import models

# Create your models here.
from customer.models import Customer
from store.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = 0
        for item in order_items:
            total += item.get_total
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = 0
        for item in order_items:
            total += item.quantity
        return total

    def __str__(self):
        return f'{self.id}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    province = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    postal_code = models.CharField(max_length=225)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
