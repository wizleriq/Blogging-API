from django.urls import path
from .views import RegisterView, PostListCreateView, PostDetailView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("posts/", PostListCreateView.as_view(), name="create-post"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_details")
]