from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import PostForm, UpdateForm, ShareForm
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
        post = self.object  # Directly using the object from DetailView
        total_likes = post.total_likes()
        total_dislikes = post.total_dislikes()
        total_share = post.shares.count()

        # Checking if the user has liked the post
        liked = post.likes.filter(id=self.request.user.id).exists()
        disliked = post.dislikes.filter(id=self.request.user.id).exists()

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["total_dislikes"] = total_dislikes
        context["liked"] = liked
        context["disliked"] = disliked
        context["totaL_share"] = total_share
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
        cat_menu_list = Category.objects.all()
        return render(request, self.template_name, {"cat_menu_list": cat_menu_list})


class LikeView(LoginRequiredMixin, View):
    login_url = "/login/"  # Optional: Redirect to login page if not authenticated

    @staticmethod
    def post(request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))


class DislikeView(LoginRequiredMixin, View):
    login_url = "/login/"  # Optional: Redirect to login page if not authenticated

    @staticmethod
    def post(request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)
        return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))


class ShareView(View):
    @staticmethod
    def get(request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = ShareForm()
        return render(request, "myblog/share_post.html", {"form": form, "post": post})

    @staticmethod
    def post(request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = ShareForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))
        return render(request, "myblog/share_post.html", {"form": form, "post": post})
