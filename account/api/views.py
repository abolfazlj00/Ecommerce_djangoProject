import re
from string import ascii_letters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.api.serializers import RegistrationSerializer
from account.models import CustomUser
from customer.models import Customer


def usernameValidation(username):
    for letter in username:
        if letter not in ascii_letters and letter != '_' and letter not in '0123456789':
            error = 'please use only letters (a-z,A-Z), numbers, or underline for username'
            return error
    try:
        if CustomUser.objects.get(username=username):
            error = 'This username has already existed'
            return error
    except CustomUser.DoesNotExist:
        return 'True'


def passwordValidation(password):
    if len(password) < 8:
        error = 'password is too short. It must be at least 8 characters'
        return error
    for letter in password:
        if letter not in ascii_letters and letter not in '0123456789':
            error = 'please use only letters (a-z,A-Z), numbers for password'
            return error
    return 'True'


def phoneValidation(phone):
    regex_for_phone = r"^(\+98?)?{?(0?9[0-9]{9,9}}?)$"
    if not re.search(regex_for_phone, phone):
        error = "phone is not valid !"
        return error
    try:
        if CustomUser.objects.get(phone=phone):
            error = 'This phone has already existed'
            return error
    except CustomUser.DoesNotExist:
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


def registerUser(request, username, password, phone, email=None):
    validation_response = registerValidation(username, password, phone, email=email)
    if validation_response == 'True':
        return 'True'
    else:
        error = validation_response
        return error


@api_view(['POST', ])
def registrationView(request):
    data = {}
    if request.method == 'POST':
        try:
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=False)
            username = request.data['username']
            password = request.data['password']
            phone = request.data['phone']
            email = request.data['email']
            resp = registerUser(request, username, password, phone, email)
            if resp == 'True':
                user = serializer.save()
                createCustomer(user)
                data['username'] = username
                data['password'] = password
                # return loginUser(request, username, password)
            data['resp'] = resp
            return Response(data)
        except:
            data['wrong input'] = 'Wrong Input'
            return Response(data)


def createCustomer(user):
    new_customer = Customer(user=user)
    new_customer.save()
    print(Customer.objects.all())
