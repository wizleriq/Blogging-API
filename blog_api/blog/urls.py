from django.urls import path
from .views import RegisterView, PostListCreateView, PostDetailView, CommentListCreateAPIView, CommentDetail

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("posts/", PostListCreateView.as_view(), name="create-post"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_details"),
    path("comments/", CommentListCreateAPIView.as_view(), name='comments'),
    path("comments/<int:pk>/", CommentDetail.as_view(), name='user-coments')
]