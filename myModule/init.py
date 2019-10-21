from category.models import Category
from post.models import Post


def init():
    categorys = Category.objects.all();

    for category in categorys :
        category.post_num = Post.objects.filter(category=category, use_tf=True).count()
        category.save()