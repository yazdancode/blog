from django import forms
import re
from .models import Post
from datetime import date


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author", "body")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": (
                        "color: #1a202c; font-size: 16px; font-weight: 600;"
                        "margin-bottom: 2rem; padding-bottom: 10px;"
                        "border-bottom: 2px solid #e2e8f0;"
                    ),
                    "placeholder": "عنوان را اینجا وارد کنید",
                }
            ),
            "title_tag": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "color: #303b51; font-size: 16px; font-weight: 600;",
                    "placeholder": "برچسب عنوان را اینجا وارد کنید",
                }
            ),
            "author": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": (
                        "color: #1a202c; font-size: 14px; font-weight: 400;"
                        "line-height: 1.5; padding: 10px;"
                    ),
                    "placeholder": "متن پست را اینجا وارد کنید",
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("عنوان باید حداقل ۵ کاراکتر باشد.")
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", title):
            raise forms.ValidationError("عنوان نباید شامل کاراکترهای خاص باشد.")
        if not re.match(r"^[\u0600-\u06FF\s]+$", title):
            raise forms.ValidationError("عنوان باید فقط شامل حروف فارسی باشد.")
        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError("این عنوان قبلاً ثبت شده است.")
        return title

    def clean_title_tag(self):
        title_tag = self.cleaned_data.get("title_tag")
        if len(title_tag) > 50:
            raise forms.ValidationError("برچسب عنوان نباید بیش از ۵۰ کاراکتر باشد.")
        if not re.match(r"^[\u0600-\u06FF\s]+$", title_tag):
            raise forms.ValidationError("برچسب عنوان باید فقط شامل حروف فارسی باشد.")
        return title_tag

    def clean_author(self):
        author = self.cleaned_data.get("author")
        if not author:
            raise forms.ValidationError("نویسنده باید مشخص شود.")
        return author

    def clean_body(self):
        body = self.cleaned_data.get("body")
        banned_words = ["نامناسب", "غیرمجاز", "کلمه‌بد"]
        for word in banned_words:
            if word in body:
                raise forms.ValidationError(f"متن پست نباید شامل کلمه '{word}' باشد.")
        if not re.match(r"^[\u0600-\u06FF\s]+$", body):
            raise forms.ValidationError("متن باید فقط شامل حروف فارسی باشد.")
        if not body.strip():
            raise forms.ValidationError("متن پست نمی‌تواند فقط شامل فاصله باشد.")
        word_count = len(body.split())
        if word_count < 10:
            raise forms.ValidationError("متن پست باید حداقل ۱۰ کلمه داشته باشد.")
        if word_count > 500:
            raise forms.ValidationError("متن پست نباید بیش از ۵۰۰ کلمه باشد.")
        return body

    def clean_publish_date(self):
        publish_date = self.cleaned_data.get("publish_date")
        if publish_date > date.today():
            raise forms.ValidationError("تاریخ انتشار نمی‌تواند در آینده باشد.")
        return publish_date
