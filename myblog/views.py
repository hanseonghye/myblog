from django.shortcuts import render
from django.views.generic import TemplateView
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



def handler400(request):
    return render(request, "error.html", status = 400)


def handler403(request):
    return render(request, "error.html", status = 403)


def handler404(request):
    return render(request, "error.html", status = 404)


def handler500(request):
    return render(request, "error.html", status = 500)