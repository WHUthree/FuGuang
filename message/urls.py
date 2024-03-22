from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('groupchat/<int:gid>/',views.show),
    path('groupchat/<int:gid>/<int:uid>/',views.send),
    path('notifications/unread/<int:uid>/',views.unread),
    path('notifications/read/<int:uid>/',views.read)
]
