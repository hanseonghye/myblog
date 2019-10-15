from django.views.generic import DetailView
from post.models import Post


class PostDV(DetailView):
    model = Post
    template_name = 'post/detail.html'
    lookup_field = 'pk'
