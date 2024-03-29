"""
URL configuration for FuGuang project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import notifications.urls
from common.db import FileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('user.urls')),
    re_path(r'file/image/(.+?)/', FileView.as_view()),
    path("api/square/", include("square.urls")),
    path("api/chat/", include("message.urls")),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
