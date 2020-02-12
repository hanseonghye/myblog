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



def handler400(request, exception):
    data =dict()
    data['status'] = 400
    return render(request, "myblog/error.html", data)


def handler403(request, exception):
    data =dict()
    data['status'] = 403
    return render(request, "myblog/error.html", data)


def handler404(request, exception):
    data =dict()
    data['status'] = 404
    return render(request, "myblog/error.html", data)


def handler500(request):
    data =dict()
    data['status'] = 500
    return render(request, "myblog/error.html", data)