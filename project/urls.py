"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from categories.views import categories_by_gender_render
from people.views import genders_render
from products.views import products_list_by_category_render, product_detail
from project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', genders_render),
    path('categories/<int:gender>', categories_by_gender_render),
    path('products/<int:category>', products_list_by_category_render),
    path('product_detail/<int:product>', product_detail)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
