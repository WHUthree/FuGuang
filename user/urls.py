from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from user.views import LoginView, UserView, RegisterView
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('user', UserView, )

urlpatterns = [
    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 下面这个是用来验证token的，根据需要进行配置
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view()),
]

urlpatterns += routers.urls
