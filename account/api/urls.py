from django.urls import path
from account.api.views import registrationView, changePassword

app_name = 'api_account'
urlpatterns = [
    path('register/', registrationView, name='registration'),
    path('change-password/<str:username>/', changePassword, name='change-password')
]