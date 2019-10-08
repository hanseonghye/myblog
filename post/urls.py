from django.urls import path

from post.views import PostDV2

urlpatterns = [
    path('<int:pk>', PostDV2.as_view(), name='detail'),
]