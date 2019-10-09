from django.urls import path

from post.views import PostDV

app_name = "post"

urlpatterns = [
    path('<int:pk>', PostDV.as_view(), name='index'),
]