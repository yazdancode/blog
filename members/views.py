from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


# ثبت‌نام کاربر
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")  # بعد از ثبت‌نام به صفحه ورود هدایت می‌شود


# ورود کاربران
# class ProfileView(FormView):
#     template_name = "registration/login.html"
#     form_class = ProfileForm
#     success_url = reverse_lazy("home")
#
#     def form_valid(self, form):
#         form.save()
#         return redirect(self.success_url)
#
#
# # خروج کاربران
# class UserLogoutView(LogoutView):
#     next_page = reverse_lazy("login")  # مسیر پس از خروج
