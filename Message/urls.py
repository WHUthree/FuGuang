from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #发送get请求 /?gid=
    path('chat/',views.show)
]