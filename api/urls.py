from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'product'

router = routers.DefaultRouter()
router.register('products', views.ProductViewset)
router.register('categories', views.CategoryViewset)
# router.register('categories_detail', views.CategoryDetailViewset)





urlpatterns = [
    path('', include(router.urls)),
    path(
'product/<pk>/like/',
views.ProductCreateView.as_view(),
name='product_like'
),

]