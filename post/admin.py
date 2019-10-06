from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from post.models import Post

admin.site.register(Post, MarkdownxModelAdmin)
