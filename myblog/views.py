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

    def get_context_data(self, *args, **kwargs):
        cat_menu = super().get_context_data(**kwargs)
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(BaseView, DetailView):
    template_name = "myblog/article_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = super().get_context_data(**kwargs)
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context


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
        category = get_object_or_404(Category, slug=category_name)
        posts = Post.objects.filter(category=category)

        return render(
            request, self.template_name, {"category": category, "posts": posts}
        )


class CategoryListView(View):
    template_name = "myblog/category_list.html"

    def get(self, request):
        # گرفتن تمام دسته‌بندی‌ها
        cat_menu_list = Category.objects.all()
        return render(request, self.template_name, {"cat_menu_list": cat_menu_list})
