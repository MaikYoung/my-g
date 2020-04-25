from django.contrib import admin
from django.utils.safestring import mark_safe

from philosophy.models import Philosophy


class PhilosophyAdmin(admin.ModelAdmin):
    list_display = ('speech', 'youtube_url')


admin.site.register(Philosophy, PhilosophyAdmin)
