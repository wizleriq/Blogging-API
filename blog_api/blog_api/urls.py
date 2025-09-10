"""
URL configuration for blog_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse ("Welcome to Blogging API") 

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),

    # JWT auth
    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),

    path("auth/", include("blog.urls")),  # Include your app urls here
    

    # Djoser endpoints
    path('auth/', include('djoser.urls')),  # user management
    path('auth/', include('djoser.urls.jwt')) # JWT-specific endpoints
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)