from django.urls import path
from account.api.views import registrationView, changePassword
from store.api.views import ProductList, CategoryList

app_name = 'api_store'
urlpatterns = [
    path('products/', ProductList.as_view()),
    path('categories/', CategoryList.as_view()),
]