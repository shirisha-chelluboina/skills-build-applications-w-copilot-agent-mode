"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse
from . import views

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'users', views.UserProfileViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)
router.register(r'workouts', views.WorkoutViewSet)

def codespace_api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    api_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({"api_root": api_url})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', codespace_api_root, name='codespace-api-root'),
    path('', views.api_root, name='api-root'),
]
