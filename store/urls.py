from django.urls import path

from store.views import baseView, deepCategoryView

app_name = 'store'
urlpatterns = [
    path('', baseView, name='home'),
    path('category/all/<int:cat_id>', deepCategoryView, name='deep_category'),
]
