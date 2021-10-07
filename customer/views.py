from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from customer.models import Customer
from order.models import ShippingAddress


@login_required
def address(request):
    if request.method == 'POST':
        customer = request.user
        province = request.POST['province']
        city = request.POST['city']
        user_address = request.POST['address']
        postal_code = request.POST['postal_code']
        new_address = ShippingAddress(customer=customer, province=province, city=city, address=user_address, postal_code=postal_code)
        new_address.save()
        return HttpResponse('True')
