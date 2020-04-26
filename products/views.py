from django.shortcuts import render

from products.models import Product


def products_list_by_category_render(request, category):
    products = Product.objects.filter(category=category).filter(available=True)\
        .only('name_to_show', 'image_to_show', 'price')
    context = {'products': products}
    return render(request, 'products/product_list.html', context)


def product_detail(request, product):
    product = Product.objects.filter(available=True).get(id=product)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
