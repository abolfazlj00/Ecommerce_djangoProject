from django.urls import path

from customer.views import address

app_name = 'customer'
urlpatterns = [
    path('addresses/', address, name='address'),
]