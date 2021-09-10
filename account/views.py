import re
from django.contrib.auth import authenticate
from django.http import response
from django.shortcuts import render
from string import ascii_letters


def usernameValidation(username):
    for letter in username:
        if letter not in ascii_letters and letter != '_' and letter not in range(0, 10):
            error = 'please use only letters (a-z,A-Z), numbers, or underline for username'
            return error
    return 'True'


def passwordValidation(password):
    for letter in password:
        if letter not in ascii_letters and letter not in range(0, 10):
            error = 'please use only letters (a-z,A-Z), numbers for password'
            return error
    return 'True'


def phoneValidation(phone):
    regex_for_phone = r"^(\+98?)?{?(0?9[0-9]{9,9}}?)$"
    if not re.search(regex_for_phone, phone):
        error = "phone is not valid !"
        return error
    return 'True'


def emailValidation(email):
    regex_for_email = r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"
    if not re.search(regex_for_email, email):
        error = "email is not valid !"
        return error
    return 'True'


def registerValidation(username, password, phone, email=None):
    username_return = usernameValidation(username)
    if username_return != 'True':
        return username_return

    phone_return = phoneValidation(phone)
    if phone_return != 'True':
        return phone_return

    password_return = passwordValidation(password)
    if password_return != 'True':
        return password_return

    if email:
        email_return = emailValidation(email)
        if email_return != 'True':
            return email_return

    return 'True'


def register(request, username, password, phone, email=None):
    validation_response = registerValidation(username, password, phone, email=email)
    if validation_response == 'True':
        return 'True'
    else:
        error = validation_response
        return render(request, 'account/register-login.html', context={'reg_error': error, 'register': 'True'})


def login(request, username, password):
    if authenticate(username=username, password=password) or authenticate(phone=username, password=password):
        if 'next' in request.GET:
            return request.GET['next']
        return render(request, 'store/home.html')
    else:
        return render(request, 'account/register-login.html', context={
            'log_error': 'incorrect username or password'
        })


def rgisterLogin(request):
    if request.method == 'POST':
        if request.POST['type'] == 'login':
            return login(request, request.POST['username'], request.POST['password'])
        if request.POST['type'] == 'register':
            return register(request, request.POST['username'], request.POST['password'], request.POST['phone'],
                            request.POST['email'])
    return render(request, 'account/register-login.html')
