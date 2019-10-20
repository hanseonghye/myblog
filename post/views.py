from django.views.generic import DetailView, ListView
from hitcount.views import HitCountDetailView

from post.models import Post


class PostDV(HitCountDetailView):
    model = Post
    template_name = 'post/detail.html'
    lookup_field = 'pk'
    count_hit = True


class RelatedPostLV(ListView):
    model = Post
    template_name = "post/related_posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        tags = self.request.GET.getlist('tags[]')
        now_pk = self.request.GET['now_post']
        return Post.objects.filter(tags__name__in=tags).exclude(pk=now_pk)



class TagLV(ListView):
    template_name = "post/all_tags.html"
    context_object_name = 'tags'


    def get_queryset(self):
        return Post.tags.all().order_by('post__tags__num_times')


class TagPostLV(ListView):
    template_name = "post/tag_posts.html"
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__id=self.request.GET['tag_id'])
