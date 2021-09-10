from django.urls import path

from account.views import LoginUser


app_name = 'account'
urlpatterns = [
    path('sign-in/', LoginUser, name='login'),
]