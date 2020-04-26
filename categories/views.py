from django.shortcuts import render

from categories.models import Category


def categories_by_gender_render(request, gender):
    categories = Category.objects.filter(gender=gender).filter(available=True)
    context = {'categories': categories}
    return render(request, 'categories/category.html', context)
