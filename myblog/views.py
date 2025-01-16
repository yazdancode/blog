from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import PostForm, UpdateForm
from .models import Post, Category


class BaseView:
    model = Post


class BaseForm:
    form_class = PostForm


class HomeView(BaseView, ListView):
    template_name = "myblog/home.html"
    ordering = ["-post_date"]
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ArticleDetailView(BaseView, DetailView):
    template_name = "myblog/article_details.html"


class AddPostView(BaseView, BaseForm, CreateView):
    template_name = "myblog/add_post.html"


class AddCategoryView(CreateView):
    model = Category
    template_name = "myblog/add_category.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("home")


class UpdatePostView(BaseView, UpdateView):
    template_name = "myblog/update_post.html"
    form_class = UpdateForm


class DeletePostView(BaseView, DeleteView):
    template_name = "myblog/delete_post.html"
    success_url = reverse_lazy("home")


class CategoryView(View):
    template_name = "myblog/category.html"

    def get(self, request, category_name):
        # بازیابی دسته‌بندی با استفاده از نام یا برگرداندن 404 اگر پیدا نشد
        category = get_object_or_404(Category, name=category_name)
        # فیلتر کردن پست‌ها با توجه به دسته‌بندی
        posts = Post.objects.filter(category=category)
        return render(
            request, self.template_name, {"category": category, "posts": posts}
        )
