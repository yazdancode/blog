from django.urls import path
from .views import (
    HomeView,
    ArticleDetailView,
    AddPostView,
    AddCategoryView,
    UpdatePostView,
    DeletePostView,
    CategoryView,
    CategoryListView,
    LikeView,
    AddCommentView,
    UserView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("article_edit/<int:pk>", UpdatePostView.as_view(), name="update_post"),
    path("article/<int:pk>/remove", DeletePostView.as_view(), name="delete_post"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path("category/<str:cats>/", CategoryView.as_view(), name="category"),
    path("user-posts/<int:pk>/", UserView, name="user_posts"),
    path("category-list/", CategoryListView.as_view(), name="category-list"),
    path("like/<int:pk>", LikeView.as_view(), name="like_post"),
    path("article/<int:pk>/comment/", AddCommentView.as_view(), name="add_comment"),
]
