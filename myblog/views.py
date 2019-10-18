from django.shortcuts import render
from django.views.generic import TemplateView

from category.models import Category
from post.models import Post


class MainView(TemplateView):
    template_name = 'myblog/main.html'

    def get_context_data(self, **kwargs):
        data = dict();
        data['posts'] = Post.objects.filter(use_tf = True)
        return data

