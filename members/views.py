from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import login
from .forms import SignUpForm


# ثبت‌نام کاربر
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()  # Save the user object
        login(self.request, user)
        return redirect(self.success_url)


class UserEditeView(UpdateView):
    form_class = UserChangeForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

    def get_object(self, **kwargs):
        return self.request.user
