from django.contrib import admin
from django.utils.safestring import mark_safe

from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_to_show', 'gender', 'available')
    search_fields = ('name_to_show',)
    list_filter = ('gender',)
    readonly_fields = ('current_image',)

    @staticmethod
    def current_image(obj):
        to_return = f'<img src="http://127.0.0.1:8000/images/{obj.image_to_show}">'
        return mark_safe(to_return)


admin.site.register(Category, CategoryAdmin)
