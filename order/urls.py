from django.urls import path

from order.views import updateItem, cart, checkout, orderHistory, checkDiscount

app_name = 'order'
urlpatterns = [
    path('cart/', cart, name='cart'),
    path('update-item/', updateItem, name='update-item'),
    path('checkout/', checkout, name='checkout'),
    path('order-history/', orderHistory, name='order-history'),
    path('check-discount/<str:code>/', checkDiscount, name='check-discount'),
]
