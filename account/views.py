import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import response, HttpResponse
from django.shortcuts import render, redirect
from string import ascii_letters


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


@login_required
def logoutUser(request):
    logout(request)
    return redirect('store:home')


@login_required
def profile(request):
    return render(request, 'account/profile.html')

@login_required
def editProfile(request):
    if request.method == 'POST':
        return 'hi'
