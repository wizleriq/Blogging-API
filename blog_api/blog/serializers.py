from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

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
class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    # followers = UserSerializer(many=True, read_only=True)
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ['id', 'user', 'email', 'bio', 'profile_picture', 'followers', 'following']
        read_only_fields = ["user","email"]
    
    def get_followers(self, obj):
        # assuming followers is a ManyToMany to Profile
        return [profile.user.username for profile in obj.followers.all()]

    def get_following(self, obj):
        # assuming following is a ManyToMany to Profile
        return [profile.user.username for profile in obj.following.all()]
    
    # def get_following(self, obj):
    #     return [profile.user.username for profile in obj.following.all()]
    

        # fields = ['user', 'bio', 'profile_picture', 'follow']

        def get_following(self, obj):
            following_profiles = obj.following.all()
            return [
                {
                    'id': profile.user.id,
                    'username': profile.user.username,
                    'email': profile.user.email,
                }
                for profile in following_profiles
            ]
        
        def get_followers(self, obj):
            followers_profiles =obj.followers.all()
            return [
                {
                    'id': profile.user.id,
                    'username': profile.user.username,
                    'email': profile.user.email,
                }
                for profile in followers_profiles
            ]
        
        # def get_followers(self, obj):
        #     follower_profiles = obj.followers.all()


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ['id', 'post','author', 'content', 'created_at', 'updated_at']

    def __str__(self):
        return f"Comment by{self.author} on {self.post}"
       
class PostSerializer(serializers.ModelSerializer):
    # This means the field cannot be set by the client (the user making the request).
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ["id", "title", "body", "author", "created_at", "updated_at", "comments"]
        # fields = ["id", "title", "comments", "body", "author", "created_at", "updated_at"]

# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')  # show username, but not editable

#     class Meta:
#         model = Comment
#         fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

#     def __str__(self):
#         return f"Comment by {self.author} on {self.post}"


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')
#     class Meta:
#         model = Comment
#         fields = ['id', 'post','author', 'content', 'created_at', 'updated_at']

#     def __str__(self):
#         return f"Comment by{self.author} on {self.post}"
    
#     # class CommentSerializer(serializers.ModelSerializer):
#     # author = serializers.ReadOnlyField(source='author.username')  # show username, but not editable

#     # class Meta:
#     #     model = Comment
#     #     fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

#     # def __str__(self):
#     #     return f"Comment by {self.author} on {self.post}"


        
#     # 



    
    
    