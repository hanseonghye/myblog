from django.urls import path

from post.views import PostDV

urlpatterns = [
    path('<int:pk>', PostDV.as_view(), name='detail'),
]