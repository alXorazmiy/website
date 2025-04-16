
from django.urls import path
from .views import *


urlpatterns = [
    path("users/", UsersListAPIView.as_view(), name='user-list-create'),
    path("user/", UserAPIView.as_view(), name='user'),
    path("user/<int:pk>/", UserDetailAPIView.as_view(), name='user-detail'),
    path("register/", RegisterAPIView.as_view(), name = "register"),
    path("login/", LoginAPIView.as_view(), name = "login"),
    path("logout/", LogoutAPIView.as_view(), name = "logout"),
]
