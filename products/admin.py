from django.contrib import admin
from django.utils.safestring import mark_safe

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_to_show', 'category', 'stock', 'available')
    search_fields = ('name_to_show',)
    list_filter = ('category',)
    readonly_fields = ('current_image',)

    @staticmethod
    def current_image(obj):
        to_return = '<p>IMAGEN 1.</p>'
        to_return += f'<img src="http://127.0.0.1:8000/{obj.image_to_show}">'
        to_return += '<hr>'
        to_return += '<p>IMAGEN 2.</p>'
        to_return += f'<img src="http://127.0.0.1:8000/{obj.image_to_show_two}">'
        return mark_safe(to_return)

    @staticmethod
    def stock(obj):
        return obj.sizes_s + obj.sizes_m + obj.sizes_l + obj.sizes_xl + obj.sizes_xxl


admin.site.register(Product, ProductAdmin)
