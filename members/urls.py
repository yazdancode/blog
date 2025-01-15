from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    # path("login/", ProfileView.as_view(), name="login"),
    # path("logout/", UserLogoutView.as_view(), name="logout"),
]
