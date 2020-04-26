from django.contrib import admin
from django.utils.safestring import mark_safe

from people.models import Gender


class GenderAdmin(admin.ModelAdmin):
    list_display = ('name_to_show',)
    readonly_fields = ('current_image',)

    @staticmethod
    def current_image(obj):
        to_return = f'<img src="http://127.0.0.1:8000/images/{obj.image_to_show}">'
        return mark_safe(to_return)


admin.site.register(Gender, GenderAdmin)
