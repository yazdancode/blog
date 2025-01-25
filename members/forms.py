import jdatetime
from django import forms
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)
from django.contrib.auth.models import User


class BaseUserForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "ایمیل خود را وارد کنید",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "نام کوچک خود را وارد کنید",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "نام خانوادگی خود را وارد کنید",
            }
        ),
    )
    GENDER_CHOICES = [("M", "مرد"), ("F", "زن"), ("O", "سایر")]
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    age = forms.IntegerField(
        max_value=99,
        min_value=18,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "سن خود را وارد کنید",
            }
        ),
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "نام کاربری خود را وارد کنید",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "gender", "age")
        labels = {
            "username": "نام کاربری",
            "first_name": "نام کوچک",
            "last_name": "نام خانوادگی",
            "email": "ایمیل",
        }


class SignUpForm(UserCreationForm, BaseUserForm):
    class Meta(BaseUserForm.Meta):
        fields = BaseUserForm.Meta.fields + ("password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلاً ثبت شده است.")
        return email


class EditProfileForm(UserChangeForm, BaseUserForm):
    class Meta(BaseUserForm.Meta):
        exclude = ("password",)


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=50,
        min_length=8,
        label="رمز عبور فعلی",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "رمز عبور فعلی",
            }
        ),
    )
    new_password1 = forms.CharField(
        max_length=50,
        min_length=8,
        label="رمز عبور جدید",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "رمز عبور جدید",
            }
        ),
    )
    new_password2 = forms.CharField(
        max_length=50,
        min_length=8,
        label="تایید رمز عبور",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "تکرار رمز عبور جدید",
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            "old_password",
            "new_password1",
            "new_password2",
        ]
