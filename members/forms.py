from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.get("request", None)  # دریافت request اگر موجود باشد
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ("user", "password")
        widgets = {
            "user": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your username"}
            ),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Enter your password"}
            ),
        }
