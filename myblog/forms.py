import re
from django import forms
from django.core.cache import cache
from .models import Post, Category

# دریافت گزینه‌های دسته‌بندی با استفاده از حافظه پنهان
CATEGORIES_CACHE_KEY = "categories"
categories = cache.get(CATEGORIES_CACHE_KEY)
if not categories:
    categories = list(Category.objects.all().values_list("name", "name"))
    cache.set(CATEGORIES_CACHE_KEY, categories, 3600)  # ذخیره برای 1 ساعت


# تابع کمکی برای تنظیم استایل ویجت‌ها
def form_widget_attrs(base_attrs, **styles):
    """
    تنظیمات استایل ویجت را به صورت یکپارچه مدیریت می‌کند.
    """
    style_string = "; ".join(f"{k}: {v}" for k, v in styles.items())
    base_attrs["style"] = style_string
    return base_attrs


# توابع کمکی برای اعتبارسنجی متن فارسی
def validate_persian_text(text, field_name, min_length=None, max_length=None):
    """
    متن فارسی را اعتبارسنجی می‌کند.
    """
    if min_length and len(text) < min_length:
        raise forms.ValidationError(
            f"{field_name} باید حداقل {min_length} کاراکتر باشد."
        )
    if max_length and len(text) > max_length:
        raise forms.ValidationError(
            f"{field_name} نباید بیش از {max_length} کاراکتر باشد."
        )
    if not re.match(r"^[\u0600-\u06FF\s]+$", text):
        raise forms.ValidationError(f"{field_name} باید فقط شامل حروف فارسی باشد.")
    return text


def validate_no_special_chars(text, field_name):
    """
    بررسی می‌کند که متن شامل کاراکترهای خاص نباشد.
    """
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", text):
        raise forms.ValidationError(f"{field_name} نباید شامل کاراکترهای خاص باشد.")
    return text


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author", "category", "body")
        widgets = {
            "title": forms.TextInput(
                attrs=form_widget_attrs(
                    {"class": "form-control"},
                    color="#1a202c",
                    font_size="16px",
                    font_weight="600",
                    margin_bottom="2rem",
                    padding_bottom="10px",
                    border_bottom="2px solid #e2e8f0",
                )
            ),
            "title_tag": forms.TextInput(
                attrs=form_widget_attrs(
                    {
                        "class": "form-control",
                        "placeholder": "برچسب عنوان را اینجا وارد کنید",
                    },
                    color="#303b51",
                    font_size="16px",
                    font_weight="600",
                )
            ),
            "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(
                choices=categories, attrs={"class": "form-control"}
            ),
            "body": forms.Textarea(
                attrs=form_widget_attrs(
                    {
                        "class": "form-control",
                        "placeholder": "متن پست را اینجا وارد کنید",
                    },
                    color="#1a202c",
                    font_size="14px",
                    font_weight="400",
                    line_height="1.5",
                    padding="10px",
                )
            ),
        }

    def clean_title(self):
        """
        اعتبارسنجی عنوان
        """
        title = self.cleaned_data.get("title")
        title = validate_persian_text(title, "عنوان", min_length=5)
        title = validate_no_special_chars(title, "عنوان")
        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError("این عنوان قبلاً ثبت شده است.")
        return title

    def clean_title_tag(self):
        """
        اعتبارسنجی برچسب عنوان
        """
        title_tag = self.cleaned_data.get("title_tag")
        return validate_persian_text(title_tag, "برچسب عنوان", max_length=50)

    def clean_body(self):
        """
        اعتبارسنجی متن پست
        """
        body = self.cleaned_data.get("body")
        banned_words = r"نامناسب|غیرمجاز|کلمه‌بد"
        if re.search(banned_words, body):
            raise forms.ValidationError("متن پست نباید شامل کلمات نامناسب باشد.")
        body = validate_persian_text(body, "متن پست", min_length=10, max_length=500)
        if not body.strip():
            raise forms.ValidationError("متن پست نمی‌تواند فقط شامل فاصله باشد.")
        return body


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "عنوان را اینجا وارد کنید",
                }
            ),
            "title_tag": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "برچسب عنوان را اینجا وارد کنید",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "متن پست را اینجا وارد کنید",
                }
            ),
        }
