from django.shortcuts import render


def LoginUser(request):
    if request.method == 'POST':
        print('ok')
    return render(request, 'account/register-login.html')
