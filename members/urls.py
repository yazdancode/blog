from django.urls import path
from .views import UserRegisterView, UserEditeView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserEditeView.as_view(), name="edit_profile"),
]
