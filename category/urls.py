from django.urls import path

from category.views import CategoryPostLV, CategoryNamePostLV, getallcategory, GetMulCategoryLV, getpostpercategory

app_name = 'category'

urlpatterns = [
    path('getallcategory', getallcategory, name='getallcategory'),
    path('getmulcategory', getpostpercategory, name='mulcategory' ),
    path('<int:pk>', CategoryPostLV.as_view(), name='index'),
    path('<str:name>', CategoryNamePostLV.as_view(), name='index'),
]