from rest_framework import serializers

from post.models import Post


class CategoryPostSimpleSerializer(serializers.ModelSerializer):
    formatted_markdown = serializers.ReadOnlyField()
    ins_dt = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Post
        fields = (
            'pk',
            'title',
            'content',
            'ins_dt',
            'formatted_markdown',
        )
