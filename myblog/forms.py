from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author", "body")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "color: #1a202c; font-size: 16px; font-weight: 600; margin-bottom: 2rem; padding-bottom: 10px; border-bottom: 2px solid #e2e8f0;",
                    "placeholder": "Enter the title here",
                }
            ),
            "title_tag": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "color: #303b51; font-size: 16px; font-weight: 600;",
                    "placeholder": "Enter the title_tag here"

                }),
            "author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }
