from django.contrib.auth.decorators import login_required
from django.http import response, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.utils.translation import activate

from store.models import Product, Category


# return all products
def getProducts():
    return Product.objects.filter(in_stock=True)


# this function return home page
def baseView(request):
    all_products = getProducts()
    return render(request, 'store/home.html',
                  context={'all_products': all_products})


def deepCategoryView(request, cat_id):
    related_categories_id = [cat_id]
    selected_category = Category.objects.get(id=cat_id)
    categories = Category.objects.all()
    for cat in categories:
        if cat.parent_id in related_categories_id:
            related_categories_id.append(cat.id)

    selected_products = Product.objects.filter(category_id__in=related_categories_id, in_stock=True)

    p = Paginator(selected_products, 1)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, 'store/category.html',
                  context={'category': selected_category, 'products': page})
