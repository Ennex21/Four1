from django.contrib import admin
from .models import Artic2


class Artic2Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'desk', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Artic2, Artic2Admin)