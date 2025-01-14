from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm, UpdateForm


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


class UpdatePostView(UpdateView):
    model = Post
    template_name = "myblog/update_post.html"
    form_class = UpdateForm
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "myblog/delete_post.html"
    success_url = reverse_lazy("home")
