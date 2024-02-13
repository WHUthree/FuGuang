from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response

from .models import User
from .views import getOpenid


class MyCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            code = request.data.get("code", None)
            appId = request.data.get("appid", None)
            appSecret = request.data.get("appsecret", None)
            password = request.data.get("password")
            if not code and not password:
                return Response({"error: 缺少code"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            if code:
                openid = getOpenid(code, appId, appSecret)
                user = User.objects.filter(openid=openid).first()
                if not user:
                    return Response({"error: 用户不存在"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                return user
            if password:
                user = User.objects.get(Q(username=username) | Q(email=username))
                if user.check_password(password):
                    return user
        except Exception as e:
            return None