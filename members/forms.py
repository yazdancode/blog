import jdatetime
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class BaseUserForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "ایمیل خود را وارد کنید",
                "id": "email",
                "type": "email",
                "id": "email",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "نام کوچک خود را وارد کنید",
                "id": "fname",
                "type": "text",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "نام خانوادگی خود را وارد کنید",
                "id": "sname",
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
                "type": "number",
                "id": "integer",
            }
        ),
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "نام کاربری خود را وارد کنید",
                "type": "string",
                "id": "username",
            }
        ),
    )
    last_login = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "آخرین ورود",
                "id": "last_login",
                "type": "datetime-local",
            }
        ),
    )
    is_superuser = forms.BooleanField(required=False, label="is_superuser")
    is_staff = forms.BooleanField(required=False, label="is_staff")
    is_active = forms.BooleanField(required=False, label="is_active")
    date_joined = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "تاریخ عضویت",
                "id": "date_joined",
                "type": "datetime-local",
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
        help_texts = {
            "username": "نام کاربری خود را وارد کنید.",
        }


class SignUpForm(UserCreationForm, BaseUserForm):
    class Meta(BaseUserForm.Meta):
        fields = BaseUserForm.Meta.fields + ("password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلاً ثبت شده است.")
        return email

    def clean_last_login(self):
        last_login = self.cleaned_data["last_login"]
        # Converting Gregorian date to Shamsi (Jalali)
        j_date = jdatetime.datetime.fromgregorian(datetime=last_login).strftime(
            "%Y/%m/%d"
        )
        return j_date


class EditProfileForm(UserChangeForm, BaseUserForm):
    class Meta(BaseUserForm.Meta):
        exclude = ("password",)
