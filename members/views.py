from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from myblog.models import Profile

from .forms import EditProfileForm, PasswordChangingForm, SignUpForm


# ویو برای تغییر رمز عبور
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = "registration/change-password.html"
    success_url = reverse_lazy("password_sucess")  # مسیر موفقیت بعد از تغییر رمز عبور


# ویو برای ثبت‌نام کاربر
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("home")  # مسیر موفقیت بعد از ثبت‌نام

    def form_valid(self, form):
        user = form.save()  # ذخیره‌ی کاربر
        login(self.request, user)  # ورود خودکار کاربر بعد از ثبت‌نام
        return redirect(self.success_url)  # هدایت به مسیر موفقیت


# ویو برای ویرایش پروفایل کاربر
class UserEditeView(UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")  # مسیر موفقیت بعد از ویرایش پروفایل

    def form_valid(self, form):
        user = form.save()  # ذخیره‌ی تغییرات
        login(self.request, user)  # ورود مجدد کاربر برای اعمال تغییرات
        return redirect(self.success_url)  # هدایت به مسیر موفقیت

    def get_object(self, **kwargs):
        return self.request.user  # بازگرداندن کاربر فعلی برای ویرایش پروفایل


class PasswordSuccessView(TemplateView):
    template_name = "registration/password_sucess.html"


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = "regisration/user_profile.html"

    def get_context_data(self, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = [
        "bio",
        "profile_pic",
        "website_url",
        "twitter_url",
        "instagram_url",
        "pinteresst_url",
    ]
    success_url = reverse_lazy("home")
