from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "ایمیل خود را وارد کنید",
                "v-model":"email",
                "id":"email",
                "type":"email"
            }
        ),
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "نام کوچک خود را وارد کنید",
                'id':"fname",
                'text':'text',
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "نام خانوادگی خود را وارد کنید",
                "id":"sname",
                "type":"text",
            }
        ),
    )
    GENDER_CHOICES = [
        ("M", "مرد"),
        ("F", "زن"),
        ("O", "سایر")
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.Select(attrs={
            "class": "form-control"
        })
    )
    age = forms.IntegerField(
        max_value=99,
        min_value=18,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "سن خود را وارد کنید",
                "type":"number",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "gender",
            "age",
        )
        labels = {
            "username": "نام کاربری",
            "first_name": "نام کوچک",
            "last_name": "نام خانوادگی",
            "email": "ایمیل",
            "password1": "رمز عبور 1",
            "password2": "رمز عبور 2",
        }
        help_texts = {
            "username": "نام کاربری خود را وارد کنید.",
            "password1": "رمز عبور باید حداقل ۸ کاراکتر باشد.",
            "password2": "لطفاً رمز عبور را دوباره وارد کنید.",
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلاً ثبت شده است.")
        return email
    

