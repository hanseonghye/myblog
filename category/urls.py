from django.urls import path

from category.views import CategoryPostLV

urlpatterns = [
    path('<int:pk>', CategoryPostLV.as_view(), name='all-post'),
]