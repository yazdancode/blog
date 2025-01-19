from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Post Title")
    title_tag = models.CharField(
        max_length=255,
        verbose_name="Post Title Tag"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    body = models.TextField(verbose_name="Post Content")
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="coding")
    likes = models.ManyToManyField(User, related_name="blog_posts", blank=True)
    dislikes = models.ManyToManyField(User, related_name="blog_dislikes", blank=True)
    shares = models.ManyToManyField(User, related_name="shared_posts", blank=True)
    target_users = models.ManyToManyField(User, related_name="target_posts", blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]  # Newest posts first

    def __str__(self):
        return f"{self.title} | {self.author}"

    @staticmethod
    def get_absolute_url():
        return reverse("home")

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()
