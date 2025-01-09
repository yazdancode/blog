from django.views.generic import ListView,DetailView
from .models import Post

class HomeView(ListView):
	model = Post
	template_name = 'myblog/home.html'


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'myblog/article_details.html'

