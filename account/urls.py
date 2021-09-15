from django.urls import path

from account.views import rgisterLogin, logoutUser, profile

app_name = 'account'
urlpatterns = [
    path('sign-in/', rgisterLogin, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/', profile, name='profile'),
]
