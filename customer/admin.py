from django.contrib import admin

from customer.models import Customer


@admin.register(Customer)
class CategoryAdmin(admin.ModelAdmin):
    pass
