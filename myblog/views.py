from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = "myblog/home.html"


class ArticleDetailView(DetailView):
    model = Post
    template_name = "myblog/article_details.html"


class AddPostView(CreateView):
    model = Post
    template_name = "myblog/add_post.html"
    fields = "__all__"
