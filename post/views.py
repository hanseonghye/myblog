from django.shortcuts import render

from myModule.myGenerics import RetrieveAPIView
from post.models import Post
from post.serializers import PostSerializer


def post_detail(request, post_id):
    post = Post.objects.get(pk = post_id)
    return render(
        request,
        'post_detail.html',
        {
            'post' : post,
        }
    )


class PostDV(RetrieveAPIView):
    queryset = Post.objects.filter(use_tf=True)
    serializer_class = PostSerializer
    lookup_field = 'pk'
