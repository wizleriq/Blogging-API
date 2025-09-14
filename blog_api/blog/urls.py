from django.urls import path
from .views import ProfileListCreateAPIView, ProfileDetailAPIView, RegisterView, PostListCreateView, PostDetailView, CommentListCreateAPIView, CommentDetail, FollowAPIView, UnfollowAPIView

urlpatterns = [
    path("profiles/", ProfileListCreateAPIView.as_view(), name="profile-list"),
    path("profiles/<int:pk>/", ProfileDetailAPIView.as_view(), name="profile-detail"),
    path("register/", RegisterView.as_view(), name="register"),
    path("posts/", PostListCreateView.as_view(), name="create-post"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_details"),
    path("comments/", CommentListCreateAPIView.as_view(), name='comments'),
    path("comments/<int:pk>/", CommentDetail.as_view(), name='user-coments'),
    path("profiles/<int:pk>/follow/", FollowAPIView.as_view(), name="follow"),
    path("profiles/<int:pk>/unfollow", UnfollowAPIView.as_view(), name="unfollow")
]