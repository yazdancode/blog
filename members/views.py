from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class LoginmembersView(LoginView):
    template_name = "registration/login.html"
    form_class = AuthenticationForm

    def get_redirect_url(self):
        return reverse_lazy("home")

    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutmembersView(LogoutView):
    template_name = "registration/logout.html"
    next_page = reverse_lazy("login")
