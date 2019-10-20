from django.shortcuts import render
from django.views.generic import TemplateView

from category.models import Category
from post.models import Post


class MainView(TemplateView):
    template_name = 'myblog/home.html'

    def get_context_data(self, **kwargs):
        data = dict();
        data['posts'] = Post.objects.filter(use_tf = True)
        return data

class HomeView(TemplateView):
    template_name = 'myblog/home.html'

    def get_context_data(self, **kwargs):
        data = dict();
        data['posts'] = Post.objects.filter(use_tf = True)
        return data

