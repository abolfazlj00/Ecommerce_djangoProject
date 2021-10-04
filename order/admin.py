from django.contrib import admin

# Register your models here.
from order.models import Order, OrderItem, ShippingAddress


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularInline]
    model = Order


class ShippingAddressAdmin(admin.ModelAdmin):
    model = ShippingAddress


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
