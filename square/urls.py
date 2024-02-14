from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [
    # path("recruit/", recruit_messageView.as_view()),
    # path("record/", meal_recordView.as_view()),
    # path("recruit/<int:pk>/", recruit_messageDetailView.as_view()),
    # path("record/<int:pk>/",meal_recordDetailView.as_view()),
]

router = routers.DefaultRouter()
router.register('recruit', recruit_messageView)
router.register('record', meal_recordView)
router.register('left',LeftMessageView)
router.register('appraise', AppraiseView)
router.register('share', ShareView)


urlpatterns += router.urls