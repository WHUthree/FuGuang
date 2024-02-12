from django.urls import path,re_path
from square import views  # ?

urlpatterns = [
    path("ser/square/", views.recruit_messageView.as_view()),
    path("ser/square/", views.meal_recordView.as_view()),
    re_path("ser/square/(?P<pk>\d+)", views.recruit_messageDetailView.as_view()),
    re_path("ser/square/(?P<pk>\d+)", views.meal_recordDetailView.as_view()),
]
