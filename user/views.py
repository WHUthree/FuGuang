import os
from tokenize import TokenError
from uuid import uuid1
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet
from rest_framework.views import APIView
from user.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import UserPermission
#import requests


# Create your views here.
def getOpenid(code, appId, appSecret):
    """获取openid"""
    url = 'https://api.weixin.qq.com/sns/jscode2session?' \
          'appid={appid}&' \
          'secret={secret}&' \
          'js_code={code}&' \
          'grant_type=authorization_code'.format(appid=appId, secret=appSecret, code=code)
    response = requests.get(url)

    try:
        # 这里就是拿到的openid和session_key
        openid = response.json()['openid']
        session_key = response.json()['session_key']
        return (openid, session_key)
    except KeyError as e:
        return Response({'error': 'code fail'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RegisterView(APIView):
    """注册视图"""

    def post(self, request):
        code = request.data.get("code", None)
        appId = request.data.get("appid", None)
        appSecret = request.data.get("appsecret", None)
        username = request.data.get("username")
        password = request.data.get("password", None)

        openid = None
        # 校验
        if not code and not password:
            return Response({"error: 缺少code或者密码"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if User.objects.filter(username=username).first():
            return Response({"error: 用户名重复"})
        if code:
            openid = getOpenid(code, appId, appSecret)

        # 添加用户
        obj = User.objects.create_user(username=username, openid=openid, password=password)
        res = {
            'msg': '注册成功',
            'id': obj.id,
            'username': username,
            'openid': openid
        }
        return Response(res, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    """登录视图"""
    queryset = User.objects.all()
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        code = request.data.get("code", None)
        appId = request.data.get("appid", None)
        appSecret = request.data.get("appsecret", None)
        password = request.data.get("password")

        openid = None
        if not code and not password:
            return Response({"error: 缺少code"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if code:
            openid = getOpenid(code, appId, appSecret)
            user = User.objects.filter(openid=openid).first()
            # user = user.objects.first()
            if not user:
                return Response({"error: 该微信用户不存在"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            refresh = RefreshToken.for_user(user)
            res = {
                'msg': '登录成功',
                'id': user.id,
                'username': user.username,
                'admin': user.is_superuser,
                'refresh': str(refresh),
                'token': str(refresh.access_token),
            }
            return Response(res, status=status.HTTP_200_OK)

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
    permission_classes = [IsAuthenticated, UserPermission, ]

    # 上传用户头像
    @action(methods=['post'], detail=True, url_path='upload')
    def upload_avatar(self, request, *args, **kwargs):
        avatar = request.data.get('avatar')
        # 校验是否有上传文件
        if not avatar:
            return Response({'error': '上传失败文件不能为空'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 文件大小不能超过300kb
        if avatar.size > 1024 * 300:
            return Response({'error': '上传失败, 文件大小不能超过300kb'})

        avatar.name = str(uuid1()) + os.path.splitext(avatar.name)[-1]
        # 保存文件
        user = self.get_object()

        # 获取序列化对象并校验
        ser = self.get_serializer(user, data={"avatar": avatar}, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()

        return Response({'url': ser.data['avatar']})

# class MessageView():
#     pass

