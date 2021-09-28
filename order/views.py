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
    return render(request, 'order/cart.html')


@login_required
def updateItem(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['productId']
        quantity = data['quantity']

        customer = Customer.objects.get(user=request.user)
        product = Product.objects.get(id=product_id)

        try:
            order = Order.objects.get(customer=customer, complete=False)
        except Order.DoesNotExist:
            order = Order(customer=customer, complete=False)
            order.save()

        try:
            order_item = OrderItem.objects.get(order=order, product=product)
        except OrderItem.DoesNotExist:
            order_item = OrderItem(order=order, product=product)

        order_item.quantity = quantity

        order_item.save()

        if order_item.quantity <= 0:
            order_item.delete()

        return JsonResponse('Item was added', safe=False)


@login_required
def checkout(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user=request.user)
        order = Order.objects.get(customer=customer, complete=False)
        order.complete = True
        order.save()
        return JsonResponse('True', safe=False)
    return render(request, 'order/checkout.html')


@login_required
def orderHistory(request):
    return JsonResponse('history', safe=False)