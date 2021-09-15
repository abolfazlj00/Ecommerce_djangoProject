from django.contrib.auth.decorators import login_required
from django.http import response
from django.shortcuts import render

from store.models import Product


def getProducts():
    return Product.objects.all()


def baseView(request):
    all_products = getProducts()
    return render(request, 'store/home.html',
                  context={'all_products': all_products})
