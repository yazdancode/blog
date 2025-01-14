from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # اتصال به مدل User
    first_name = models.CharField(max_length=50, blank=True, null=True)  # اطلاعات اضافی
    last_name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=128)
    bio = models.TextField(blank=True, null=True)  # توضیحات درباره کاربر
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # تصویر پروفایل
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد پروفایل

    def __str__(self):
        return self.user.username
