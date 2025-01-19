from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm


# ثبت‌نام کاربر
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


# class ProfileView(FormView):
#     template_name = "registration/login.html"
#     form_class = ProfileForm
#     success_url = reverse_lazy("home")
#
#     def form_valid(self, form):
#         form.save()
#         return redirect(self.success_url)
