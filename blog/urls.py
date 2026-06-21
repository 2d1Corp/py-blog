from django.urls import path
from blog.views import PostListView, PostDetailView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/pk/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
