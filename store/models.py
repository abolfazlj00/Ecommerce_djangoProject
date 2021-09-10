from django.db import models

# Create your models here.
from account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


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
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ['-createdTime']

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.in_stock = False

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
