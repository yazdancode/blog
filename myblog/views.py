from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator


class HomeView(ListView):
    paginate_by = 5
    model = Post
    template_name = "myblog/home.html"
    cats = Category.objects.all()
    ordering = ["-post_date"]

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        User = get_user_model()
        users = User.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["users"] = users
        return context


class LikeView(View):

    @staticmethod
    def post(request, pk):
        post = get_object_or_404(Post, id=request.POST.get("post_id"))
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse("myblog/article_details", args=[str(pk)]))


class CategoryListView(ListView):
    model = Category
    template_name = "myblog/category_list.html"
    context_object_name = "cat_menu_list"


class CategoryView(View):
    @staticmethod
    def get(request, cats):
        category_name = cats.replace("-", " ")
        category_posts = Post.objects.filter(category__name=category_name)
        return render(
            request,
            "myblog/category.html",
            {"cats": category_name.title(), "category_posts": category_posts},
        )


class UserView(ListView):
    model = Post
    template_name = "myblog/user_posts.html"
    context_object_name = "user_posts"

    def get_queryset(self):
        return Post.objects.filter(author=self.kwargs["pk"])


class ArticleDetailView(DetailView):
    model = Post
    template_name = "myblog/article_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = stuff.total_likes()
        total_comments = stuff.total_comments()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["total_comments"] = total_comments
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "myblog/add_post.html"
    # fields = '__all__'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "myblog/add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("myblog/article-details", kwargs={"pk": self.kwargs["pk"]})

    # fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "myblog/add_category.html"
    fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "myblog/update_post.html"
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "myblog/delete_post.html"
    success_url = reverse_lazy("home")
