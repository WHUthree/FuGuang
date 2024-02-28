from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [
]

router = routers.DefaultRouter()
router.register('recruit', recruit_messageView)
router.register('record', meal_recordView)
router.register('left',LeftMessageView)
router.register('appraise', AppraiseView)
router.register('share', ShareView)

urlpatterns += router.urls