from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def updateItem(request):
    return JsonResponse('Item was added', safe=True)
