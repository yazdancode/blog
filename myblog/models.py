from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Post Title")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    body = models.TextField(verbose_name="Post Content")
    created_at = models.DateTimeField(default=now)  # Fixed indentation
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]  # Newest posts first

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})
