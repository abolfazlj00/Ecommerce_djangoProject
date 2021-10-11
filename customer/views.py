import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

from customer.models import Customer
from order.models import ShippingAddress


@login_required
def address(request):
    if request.method == 'POST':
        form = json.loads(request.body)
        customer = Customer.objects.get(user=request.user)
        province = form['province']
        city = form['city']
        user_address = form['address']
        postal_code = form['postal_code']
        new_address = ShippingAddress(customer=customer, province=province, city=city, address=user_address,
                                      postal_code=postal_code)
        new_address.save()
        return JsonResponse({'response': 'True', 'id': f'address_{new_address.id}'})
