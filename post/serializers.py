from rest_framework import serializers

from post.models import Post


# class PostSerializer(serializers.ModelSerializer):
#     formatted_markdown = serializers.ReadOnlyField()
#     ins_dt = serializers.DateTimeField(format="%Y-%m-%d")
#     upd_dt = serializers.DateTimeField(format="%Y-%m-%d")
#
#     class Meta:
#         model = Post
#         fields = (
#             'title',
#             'content',
#             'ins_dt',
#             'upd_dt',
#             'formatted_markdown',
#         )