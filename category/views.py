import datetime

from django.db.models.functions import ExtractWeek, ExtractDay
from django.shortcuts import render
from django.views.generic import ListView

from category.models import Category
from post.models import Post


today = datetime.datetime.now()

def getallcategory(request):
    data = dict()
    data['categorys'] =Category.objects.filter(use_tf=True)
    data['all_count'] = Post.objects.filter(use_tf = True).count
    return render(request, "myblog/set_category.html", data)



def getpostper(request):
    return render(request,"post/posts_per.html")

def getpostpercategory(request):
    data = dict()
    data['posts'] = dict()
    categorys = Category.objects.filter(use_tf = True)

    for category in categorys :
        data["posts"][category.name] = Post.objects.filter(category = category)
    return render(request, "post/per_category.html", data)


def getpostperday(request):
    data =dict()
    data['posts'] = dict()
    days = Post.objects.filter(ins_dt__month=today.month).annotate(day = ExtractDay('ins_dt')).values('day').distinct()
    for day in days :
        data['posts'][day['day']] = Post.objects.filter(ins_dt__day=day['day'])
    return render(request, "post/per_day.html", data)


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

