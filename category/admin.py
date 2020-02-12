from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from category.models import Category

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'orderlv', 'use_tf')


admin.site.register(Category, DraggableMPTTAdmin)