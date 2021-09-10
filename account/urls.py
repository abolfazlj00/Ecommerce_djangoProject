from django.urls import path

from account.views import rgisterLogin


app_name = 'account'
urlpatterns = [
    path('sign-in/', rgisterLogin, name='login'),
]