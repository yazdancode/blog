from django.contrib.auth import login
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import EditProfileForm, SignUpForm


# ثبت‌نام کاربر
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy(
        "home"
    )  # Redirect to home or a dashboard instead of login page

    def form_valid(self, form):
        user = form.save()  # Save the user
        login(self.request, user)  # Log the user in immediately after registration
        return redirect(self.success_url)  # Redirect to success_url (e.g., home page)


# ویرایش پروفایل کاربر
class UserEditeView(UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy(
        "home"
    )  # Redirect to home or another desired page after edit

    def form_valid(self, form):
        user = form.save()  # Save the updated profile
        login(self.request, user)  # Log the user in again after profile edit
        return redirect(self.success_url)  # Redirect to success_url (e.g., home page)

    def get_object(self, **kwargs):
        return self.request.user  # Use the current logged-in user for profile editing
