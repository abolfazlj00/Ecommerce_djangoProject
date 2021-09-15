from django.urls import path
from account.api.views import registrationView

app_name = 'api_account'
urlpatterns = [
    path('register/', registrationView, name='registration')
]