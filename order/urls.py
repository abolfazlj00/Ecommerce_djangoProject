from django.urls import path

from order.views import updateItem, cart, checkout, orderHistory

app_name = 'order'
urlpatterns = [
    path('cart/', cart, name='cart'),
    path('update-item/', updateItem, name='update-item'),
    path('checkout/', checkout, name='checkout'),
    path('order-history/', orderHistory, name='order-history'),
]
