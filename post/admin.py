from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms

from post.models import Post


# class PostAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#
#     class Meta:
#         model = Post
#         fields = ['title',
#                   'category',
#                   'content',
#                   'tags',
#                   'use_tf',
#                   ]
#
#
# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm


admin.site.register(Post)
