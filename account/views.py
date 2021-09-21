import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import response, HttpResponse
from django.shortcuts import render, redirect
from string import ascii_letters
from account.api.views import emailValidation
from account.models import CustomUser


def loginUser(request, username, password):
    user = authenticate(phone=username, password=password) or authenticate(username=username, password=password)
    if user:
        login(request, user)
        if 'next' in request.GET:
            return redirect(request.GET['next'])
        return redirect('store:home')
    else:
        return render(request, 'account/register-login.html', context={
            'log_error': 'incorrect username or password'
        })


def rgisterLogin(request):
    if request.method == 'POST':
        if request.POST['type'] == 'login':
            return loginUser(request, request.POST['username'], request.POST['password'])
    return render(request, 'account/register-login.html')


def ageValidation(age):
    if int(age) >= 1:
        return 'True'
    return 'Age must be a positive number'


def setInfo(request, username, first_name, last_name, age, gender, email):
    if emailValidation(email) == 'True':
        if ageValidation(age) == 'True':
            user = CustomUser.objects.get(username=username)
            user.first_name = first_name
            user.last_name = last_name
            user.age = age
            user.gender = gender
            user.email = email
            user.save()
            return 'True'
        return ageValidation(age)
    return emailValidation(email)


@login_required
def logoutUser(request):
    logout(request)
    return redirect('store:home')


@login_required
def profile(request):
    return render(request, 'account/profile.html')


@login_required
def editProfilePersonalInfo(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        edit_info_response = setInfo(request, username, first_name, last_name, age, gender, email)
        return render(request, 'account/profile.html', context={'editInfo_response': edit_info_response})


@login_required
def changePassword(request):
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse('alooooo')


def sendEmail(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        print(user)
        return HttpResponse('True')
    except:
        return HttpResponse('False')
