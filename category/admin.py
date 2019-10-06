from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'orderlv', 'use_tf')

admin.site.register(Category, CategoryAdmin)
