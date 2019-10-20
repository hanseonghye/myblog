from django.urls import path

from category.views import CategoryPostLV, CategoryNamePostLV, getallcategory, getpostpercategory, \
    getpostperday, getpostper

app_name = 'category'

urlpatterns = [
    path('getallcategory', getallcategory, name='getallcategory'),
    path('per', getpostper, name='per' ),
    path('percategory', getpostpercategory, name='percategory' ),
    path('perday', getpostperday, name='day' ),
    path('<int:pk>', CategoryPostLV.as_view(), name='index'),
    path('<str:name>', CategoryNamePostLV.as_view(), name='index'),
]