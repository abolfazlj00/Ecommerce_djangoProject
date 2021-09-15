from django.contrib import admin

# Register your models here.
from store.models import Category, Product, Staff


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'stock', 'in_stock']
    list_filter = ['in_stock']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Staff)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user']
