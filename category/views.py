from django.shortcuts import render
from django.views.generic import ListView

from category.models import Category
from post.models import Post


def getallcategory(request):
    data = dict()
    data['categorys'] =Category.objects.filter(use_tf=True)
    return render(request, "myblog/set_category.html", data)


class GetMulCategoryLV(ListView):
    template_name = 'myblog/home.html'
    model = Category
    queryset = Category.objects.filter()

class CategoryPostLV(ListView):
    template_name = 'post/list.html'
    model=Post
    context_object_name = "posts"


    def get_queryset(self):
        if self.kwargs['pk'] == 0:
            return Post.objects.filter(use_tf=True);
        else :
            return Post.objects.filter(category = self.kwargs['pk'], use_tf=True)


class CategoryNamePostLV(ListView):
    template_name = 'post/list.html'
    model=Post
    context_object_name = "posts"


    def get_queryset(self):
        return Post.objects.filter(category__name=self.kwargs['name'],use_tf=True);

