from django.contrib.auth import views as auth_views
from django.urls import path

from .views import UserEditeView, UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserEditeView.as_view(), name="edit_profile"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
