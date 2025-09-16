from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, RegisterSerializer, PostSerializer, CommentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import Post, Comment, Profile
from rest_framework.exceptions import PermissionDenied

class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # anyone can view profiles

    # link profile to logged-in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.user:
            serializer.save()
        else: 
            raise PermissionDenied("You can't edit someone else's profile")
# Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# Post List + Create
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Automatically assign logged-in user as the author
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Post Detail (Retrieve, Update, Delete)
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    
# Only allow authors to update their own posts"
    def perform_update (self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()
        else:
            raise PermissionDenied("You cant edit someone else's post")
        
# Only allow authors to delete their own posts
    def perform_destroy(self, instance):
        if self.request.user == instance.author:
            instance.delete()
        else:
            raise PermissionDenied("You cant delete someone else's post")
        
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment .objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Only allow authors to update their own comments"
    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise PermissionDenied("You can't update some's comment")
        else:
            serializer.save()

# Allow users search for post
class PostSearchAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'title', 'content', 'username']

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Only allow authors to delete their own posts"
    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied("You can't delete some's posts")
        else:
            instance.delete()

#Follow a user
class FollowAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk): # must be 'post
        profile_to_follow = get_object_or_404(Profile, pk=pk)
        my_profile = request.user.profile
        
        if profile_to_follow == my_profile:
            return Response({"error": "You can't follow yourself"}, status = status.HTTP_400_BAD_REQUEST)
        
        my_profile.following.add(profile_to_follow)
        return Response({"message": f"You are following {profile_to_follow.user.username}"})
    
#Unfollow a user
class UnfollowAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk): # must be 'post
        profile_to_unfollow = get_object_or_404(Profile, pk=pk)
        my_profile = request.user.profile

        if my_profile == profile_to_unfollow:
            return Response({"Error": "You can't unfollow your self"}, status=status.HTTP_400_BAD_REQUEST)
        
        my_profile.following.remove(profile_to_unfollow)
        return Response({"You are no longer following"}, profile_to_unfollow.user.username)
    

    


    
    
        

         


    # def perform_destroy(self, instance):
    #     # print("Request user:", self.request.user)
    #     # print("Post author:", instance.author)
    #     if self.request.user == instance.author:
    #         instance.delete()
    #     else:
    #         raise PermissionDenied("You cant delete someone else's post")


            
