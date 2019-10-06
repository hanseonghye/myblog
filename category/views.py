from rest_framework import status
from myModule.myGenerics import *
from rest_framework.response import Response

from category.serializers import CategoryPostSimpleSerializer
from post.models import Post


class CategoryPostLV(ListAPIView):
    serializer_class = CategoryPostSimpleSerializer
    def get_queryset(self):
        if self.kwargs['pk'] == 0:
            return Post.objects.filter(use_tf=True);
        else :
            return Post.objects.filter(category = self.kwargs['pk'], use_tf=True)