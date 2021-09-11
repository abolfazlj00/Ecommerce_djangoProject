from django.contrib.auth.decorators import login_required
from django.http import response
from django.shortcuts import render

from store.models import Product


def popularProduct():
    return Product.objects.all().order_by('-likes')[:5]


def getProducts():
    return Product.objects.all()


def baseView(request):
    popular_products = popularProduct()
    all_products = getProducts()
    return render(request, 'store/home.html',
                  context={'popular_products': popular_products, 'all_products': all_products})
