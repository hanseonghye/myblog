from django.urls import path

from post.views import PostDV, RelatedPostLV, TagLV, TagPostLV

app_name = "post"

urlpatterns = [
    path('<int:pk>', PostDV.as_view(), name='index'),
    path('getrelatedposts', RelatedPostLV.as_view(), name='related_posts'),
    path('alltags', TagLV.as_view(), name='tags'),
    path('tag', TagPostLV.as_view(), name='tag-posts'),
]