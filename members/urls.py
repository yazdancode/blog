from django.urls import path
from .views import UserRegisterView, LoginmembersView, LogoutmembersView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", LoginmembersView.as_view(), name="login"),
    path("logout/", LogoutmembersView.as_view(), name="logout"),
]
