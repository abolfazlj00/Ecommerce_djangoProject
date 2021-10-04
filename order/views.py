import json
from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.messages.storage import session
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from customer.models import Customer
from order.models import Order, OrderItem
from store.models import Product


# this is a function that just return cart of customer that logged in.
def cart(request):
    return render(request, 'order/cart.html')


# this is a function for update order & orderItem of customer
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


# this is for checkout the order for customer and complete the order
@login_required
def checkout(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user=request.user)
        order = Order.objects.get(customer=customer, complete=False)
        order.complete = True
        order.save()
        return JsonResponse('True', safe=False)
    return render(request, 'order/checkout.html')


# this function return history of orders for 10 days ago
# orders must be completed.
@login_required
def orderHistory(request):
    login_user = request.user
    customer = Customer.objects.get(user=login_user)
    t = timedelta(days=10)
    ten_days_ago = datetime.now() - t
    available_orders = Order.objects.filter(customer=customer, date_ordered__range=[ten_days_ago, datetime.now()], complete=True)
    return render(request, 'order/order_history.html', context={
        'available_orders': available_orders
    })
