from django.urls import path

from order.views import updateItem, cart

app_name = 'order'
urlpatterns = [
    path('cart/', cart, name='cart'),
    path('update-item/', updateItem, name='update-item'),
]
