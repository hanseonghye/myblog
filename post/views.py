from django.views.generic import DetailView, ListView
from post.models import Post


class PostDV(DetailView):
    model = Post
    template_name = 'post/detail.html'
    lookup_field = 'pk'


class PostLV(ListView):
    model = Post
    template_name = 'myblog/home.html'
    queryset = Post.objects.