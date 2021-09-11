from django.urls import path

from store.views import baseView

app_name = 'store'
urlpatterns = [
    path('', baseView, name='home'),
]
