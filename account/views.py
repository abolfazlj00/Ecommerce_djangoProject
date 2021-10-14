import re
import uuid
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import response, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from string import ascii_letters

from django.utils.translation import activate

from account.api.views import emailValidation, passwordValidation
from account.models import CustomUser
from django.conf import settings

from order.models import ShippingAddress


def loginUser(request, username, password):
    user = authenticate(phone=username, password=password) or authenticate(username=username, password=password)
    if user:
        login(request, user)
        if 'next' in request.POST:
            return redirect(request.POST['next'])
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
    if int(age) <= 0:
        return 'Age must be a positive number'
    return 'True'


def setInfo(request, username, first_name, last_name, age, gender, email):
    if emailValidation(email) == 'True':
        if age == '' or age is None:
            age = None
            user = CustomUser.objects.get(username=username)
            user.first_name = first_name
            user.last_name = last_name
            user.age = age
            user.gender = gender
            user.email = email
            user.save()
            login(request, user)
            return 'True'
        if ageValidation(age) == 'True':
            user = CustomUser.objects.get(username=username)
            user.first_name = first_name
            user.last_name = last_name
            user.age = age
            user.gender = gender
            user.email = email
            user.save()
            login(request, user)
            return 'True'
        return ageValidation(age)
    return emailValidation(email)


@login_required
def logoutUser(request):
    logout(request)
    return redirect('store:home')


@login_required
def profile(request, editInfo_response=None):
    addresses = ShippingAddress.objects.filter(customer__user=request.user)
    context = {'addresses': addresses, 'editInfo_response': editInfo_response}
    return render(request, 'account/profile.html', context=context)


@login_required
def changeLang(request):
    activate(request.GET.get('lang'))
    return render(request, 'account/profile.html', context={'lang': True})


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
        return profile(request, edit_info_response)
        # return render(request, 'account/profile.html', context={'editInfo_response': edit_info_response})


def secretEmail(email):
    for i in range(len(email)):
        if email[i] == '@':
            j = i - 4
            secret_email = email[:4] + '*' * j + email[i:]
            return secret_email


def sendForgetPassMail(email, user):
    token = user.forget_pass_token
    subject = 'Your reset password link'
    message = f'Hi, click on the link to reset your password http://127.0.0.1:8000/account/reset-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True


def sendEmail(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        secret_user_email = secretEmail(user.email)
        if user.email == '':
            return HttpResponse('There is not any email for this username !!!')
        else:
            token = str(uuid.uuid4())
            user.forget_pass_token = token
            user.save()
            sendForgetPassMail(user.email, user)
            return HttpResponse(f'An email sent to {secret_user_email}')
    except Exception as e:
        print(e)
        return HttpResponse('This username is not exist !!!')


def resetPassword(request, token):
    try:
        user_obj = CustomUser.objects.get(forget_pass_token=token)
        user_obj.forget_pass_token = ''
        user_obj.save()
        if request.method == 'POST':
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password != confirm_password:
                error = 'The password and its confirm do not match'
                return render(request, 'account/reset_password.html', context={'error': error})
            if passwordValidation(password) == 'True':
                user_obj.password = password
                message = 'Your password changed successfully :)'
                return render(request, 'account/reset_password.html', context={'message': message})
        context = {
            'user_obj': user_obj
        }
        return render(request, 'account/reset_password.html', context)
    except:
        return HttpResponse('Not user found !!!')


@login_required
def deleteAddress(request, address_id):
    user_address = ShippingAddress.objects.get(id=address_id)
    user_address.delete()
    return JsonResponse({'data': 'True'})
