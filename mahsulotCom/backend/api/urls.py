from django.urls import path 

from api.views.shop.shopView import ShopAPIView,ShopDetailAPIView
from api.views.product.productView import ProductAPIView,ShopProductsAPIView,ProductDetailAPIView
from api.views.login.loginView import LoginAPIView
from api.views.image.imageView import ImageAPIView
from api.views.category.categoryView import CategoryAPIView
from api.views.users.usersView import UsersAPIView, UserDetailAPIView


urlpatterns = [
    path('shops/', ShopAPIView.as_view()),
    path('shops/<int:pk>/', ShopDetailAPIView.as_view()),


    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', ShopProductsAPIView.as_view()),
    path('productdetail/<int:pk>/',ProductDetailAPIView.as_view()),

    path('users/', UsersAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),

    path('category/', CategoryAPIView.as_view()),

    path('login/', LoginAPIView.as_view()),
    path('image/', ImageAPIView.as_view()),
]