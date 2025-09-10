from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post

# To register new users even when i have djoser installed.
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_picture', 'follow']

class PostSerializer(serializers.ModelSerializer):
    # This means the field cannot be set by the client (the user making the request).
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ["id", "title", "body", "author", "created_at", "updated_at"]
