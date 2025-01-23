from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Post Title")
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, verbose_name="Post Title Tag")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    # body = models.TextField(verbose_name="Post Content")
    body = HTMLField(blank=True, null=True, verbose_name="Post Content")
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorized")
    snippet = models.CharField(max_length=255)
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
