from django.contrib.auth import authenticate
from django.http import response
from django.shortcuts import render

# def registerValidation():
#
#
# def register(request, username, password, firstname, lastname, email=None):
#

def login(request,username, password):
    if authenticate(username=username, password=password) or authenticate(phone=username, password=password):
        return render(request, 'store/home.html')
    else:
        print('ascnkjasc')


def rgisterLogin(request):
    if request.method == 'POST':
        if request.POST['type'] == 'login':
            login(request,request.POST['username'], request.POST['password'])
        if request.POST['type'] == 'register':
            print('not ok')
    return render(request, 'account/register-login.html')
