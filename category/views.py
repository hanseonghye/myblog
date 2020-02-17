from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView

from category.models import Category
from post.models import Post


def getallcategory(request):
    data = dict()
    data['categorys'] = Category.objects.filter(use_tf=True).annotate(posts_count=Count('post')).order_by('tree_id', 'level', 'orderlv')
    data['all_count'] = Post.objects.filter(use_tf=True).count
    return render(request, "myblog/set_category.html", data)


class CategoryPostLV(ListView):
    template_name = 'post/list.html'
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        if self.kwargs['pk'] == 0:
            return Post.objects.filter(use_tf=True)
        else:
            return Post.objects.filter(category=self.kwargs['pk'], use_tf=True)

    def get_context_data(self, *args, **kwargs):
        data = super(CategoryPostLV, self).get_context_data(*args, **kwargs)

        if self.kwargs['pk'] == 0:
            data['all_category'] = '_ALL'
        else:
            data['category'] = Category.objects.get(id=self.kwargs['pk'])
        return data


class CategoryNamePostLV(ListView):
    template_name = 'post/list.html'
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(category__name=self.kwargs['name'], use_tf=True)

    def get_context_data(self, *args, **kwargs):
        data = super(CategoryNamePostLV, self).get_context_data(*args, **kwargs)
        data['category'] = Category.objects.get(name=self.kwargs['name'])
        return data
