from django.urls import path

from account.views import rgisterLogin, logoutUser

app_name = 'account'
urlpatterns = [
    path('sign-in/', rgisterLogin, name='login'),
    path('logout/', logoutUser, name='logout'),
]
