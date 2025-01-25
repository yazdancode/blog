from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    UserEditeView,
    UserRegisterView,
    PasswordsChangeView,
    PasswordSuccessView,
    ShowProfilePageView,
    EditProfilePageView
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserEditeView.as_view(), name="edit_profile"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password/", PasswordsChangeView.as_view(), name="password_change"),
    path("password_sucess/", PasswordSuccessView.as_view(), name="password_sucess"),
    path("<int:pk>/profile/", ShowProfilePageView.as_view(), name="show_profile_page"),
    path("<int:pk>/edit_profile_page/", EditProfilePageView.as_view(), name="edit_profile_page"),
]
