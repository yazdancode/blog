from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    model = Post
    template_name = "myblog/home.html"


class ArticleDetailView(DetailView):
    model = Post
    template_name = "myblog/article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "myblog/add_post.html"
    # fields = '__all__'
    # fields = ('title', 'body')
