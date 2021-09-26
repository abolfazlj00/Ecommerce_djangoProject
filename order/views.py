import json

from django.contrib.auth.decorators import login_required
from django.contrib.messages.storage import session
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from customer.models import Customer
from order.models import Order, OrderItem
from store.models import Product


def cart(request):
    #
    # if request.user.is_authenticated:
    #     customer = Customer.objects.get(user__username=request.user.username)
    #     order, created = Order.objects.get(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    #
    # else:
    #     pass
    return render(request, 'order/cart.html')


def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    username = request.user.username
    customer = Customer.objects.get(user__username=username)
    product = Product.objects.get(id=product_id)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)
