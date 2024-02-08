from tokenize import TokenError

from django.shortcuts import render
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.viewsets import mixins
from User.models import User
from rest_framework.permissions import IsAuthenticated
import requests

# Create your views here.
def getOpenid(code, appId, appSecret):
    """获取openid"""
    url = "https://api.weixin.qq.com/sns/jscode2session"
    url += "?appid=" + appId
    url += "&secret=" + appSecret
    url += "&js_code=" + code
    url += "&grant_type=authorization_code"
    response = requests.get(url)
    try:
        # 这里就是拿到的openid和session_key
        openid = response.json()['openid']
        session_key = response.json()['session_key']
        return (openid, session_key)
    except KeyError:
        return Response({'code': 'fail'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RegisterView(APIView):
    def post(self, request):
        code = request.data.get("code", None)
        appId = request.data.get("appid", None)
        appSecret = request.data.get("appsecret", None)
        username = request.data.get("username")

        # 校验
        if not code:
            return Response({"error: 缺少code"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if not username:
            return Response({"error"})
        openid = getOpenid(code, appId, appSecret)

        # 添加用户
        obj = User.objects.create_user(username=username, openid=openid)
        res = {
            'id': obj.id,
            'username': username,
            'openid': openid,
            'msg': '注册成功'
        }
        return Response(res, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    queryset = User.objects.all()
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        code = request.data.get("code", None)
        appId = request.data.get("appid", None)
        appSecret = request.data.get("appsecret", None)
        if not code:
            return Response({"error: 缺少code"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        openid = getOpenid(code, appId, appSecret)
        user = User.objects.filter(openid=openid)
        if not user:
            return Response({"error: 用户不存在"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        result = serializer.validated_data

        return Response(result, status=status.HTTP_200_OK)



class UserView(ModelViewSet):
    # 基本用户信息查询
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]






