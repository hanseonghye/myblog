from django.urls import path

from category.views import CategoryPostLV, CategoryNamePostLV, getallcategory, getpostpercategory, \
    getpostperday

app_name = 'category'

urlpatterns = [
    path('getallcategory', getallcategory, name='getallcategory'),
    path('getmulcategory', getpostpercategory, name='percategory' ),
    path('getperday', getpostperday, name='day' ),
    path('<int:pk>', CategoryPostLV.as_view(), name='index'),
    path('<str:name>', CategoryNamePostLV.as_view(), name='index'),
]