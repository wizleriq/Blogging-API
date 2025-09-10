from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import Post
from rest_framework.exceptions import PermissionDenied

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

    # def perform_destroy(self, instance):
    #     # print("Request user:", self.request.user)
    #     # print("Post author:", instance.author)
    #     if self.request.user == instance.author:
    #         instance.delete()
    #     else:
    #         raise PermissionDenied("You cant delete someone else's post")




            
