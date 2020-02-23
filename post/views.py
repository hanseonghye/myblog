import datetime

from django.db.models.functions import ExtractDay
from django.shortcuts import render
from django.views.generic import ListView
from hitcount.views import HitCountDetailView

from category.models import Category
from post.models import Post

today = datetime.datetime.now()


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
        now_pk = self.request.GET['now_post']
        post = Post.objects.get(pk=now_pk)
        tags = post.get_tag.filter()
        if len(tags) > 0:
            posts = Post.objects.filter(use_tf=True, tags__in=tags).exclude(pk=now_pk).distinct("pk")
            return posts

        return None


class TagLV(ListView):
    template_name = "post/all_tags.html"
    context_object_name = 'tags'

    def get_queryset(self):
        # post =
        return Post.tags.all().order_by('post__tags__num_times')


class TagPostLV(ListView):
    template_name = "post/tag_posts.html"
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(use_tf=True, tags__id=self.request.GET['tag_id'])


def getpostper(request):
    return render(request, "post/posts_per.html")


def getpostpercategory(request):
    data = dict()
    data['posts'] = dict()
    categorys = Category.objects.filter(use_tf=True)

    for category in categorys:
        data["posts"][category.name] = Post.objects.filter(use_tf=True, category=category)
    return render(request, "post/per_category.html", data)


def getpostperday(request):
    data = dict()
    data['posts'] = dict()
    days = Post.objects.filter(use_tf=True, ins_dt__month=today.month).annotate(day=ExtractDay('ins_dt')).values(
        'day').distinct()
    for day in days:
        data['posts'][day['day']] = Post.objects.filter(use_tf=True, ins_dt__day=day['day'])
    return render(request, "post/per_day.html", data)
