from django.contrib import admin

from .models import *


@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status', 'cost']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body', 'cost']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

