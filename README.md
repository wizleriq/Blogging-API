# Blogging-API
Blogging API built with Python, Django, and MySQL
BLOGGING API
Creating a Bloggong API using Python, Django and MySQL
STEP 1:
a.Create django project: Django-admin startproject Blogging_API
b.Create django app: Python manage,py startapp Blog
c.Install Djangorestframework: pip install djangorestframework
d.Go to setting.py and include the app you created, rest_framework and rest_framework.authtoken as part of installed apps also configure rest_framework and set up media files (for profile picture and post image): 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'rest_framework',
    'rest_framework.authtoken'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHNTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framwork.permissions.IsAuthenticatedOrReadOnly'
    ),
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


e.Run migrations: Python manage.py makemigrations then python manage.py migrate
f.Create superuser: Python manage.py create superuser
g.Run server: Python manage.py runserver

STEP 2:  User Registration and Authentication: models, serializer, viewset, url (endpoints)
1.I can use the default User model (django.contrib.auth.models.User) or create a custom user model if need extra fields. Or I can use Djoser 

USING DJOSER: I suggested using Djoser, which is a Django package that provides ready-made endpoints for:
POST /auth/users/ → user registration (sign up)
POST /auth/token/login/ → obtain authentication token (login)
This handles creating users and issuing tokens without you having to write custom views or serializers.

STEPS: 
1.Pip install djoser
2.Pip install djangorestframework-simplejwt
3.Configure djoser setting:     
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    ...
    'rest_framework',
    'rest_framework.authtoken',  # required by djoser
    'djoser',
    'blog',  # your app
]

4.Configure REST Framework with JWT:
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}

5.Optional JWT settings (in settings.py)
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

6.Configure URLs (urls.py)
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT auth
    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),

    # Djoser endpoints
    path('auth/', include('djoser.urls')),           # user management
    path('auth/', include('djoser.urls.jwt')),       # JWT-specific endpoints
]

7.Run migrations: Python manage.py makemigrations, python manage.py migrate

8.Test the endpoints: 
POST /auth/users/
Content-Type: application/json

{
    "username": "alice",
    "email": "alice@example.com",
    "password": "strongpassword"
}

9.Login (JWT)
POST /auth/jwt/create/
Content-Type: application/json

{
    "username": "alice",
    "password": "strongpassword"
}
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}

10.Create a Serializer
11.Create a view 
12.Create a url.py: Write it up here (not project level url.py)
Blog/url.py  
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]
13.Include it in your project level url.py ie. BLOG_API.url.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse ("Welcome Home")

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path('api/',include ('api.urls'))
]

14.RUN step 8 and 9


STEP 3: Blog Post Management

1.Create a model.py file:
Class Create(models.Model):
name: models.Charfield(max_length=100)




