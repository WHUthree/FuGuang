from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class UserSerializer(serializers.ModelSerializer):
    # 用户详细信息
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "wechat",
            "student_number",
            "avatar",
            "gender",
            "grade",
            "is_superuser",
        ]


class UserinfoSerializer(serializers.ModelSerializer):
    # 修改和创建用户
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "wechat",
            "student_number",
            "avatar",
            "gender",
            "grade",
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(max_length=150, allow_blank=True, required=False, allow_null=True)

    # 添加openid进入token信息
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # 增加想要加到token中的信息
        token["openid"] = user.openid
        return token

    # '自定义返回格式'
    def validate(self, attrs):
        # attrs.update({'password': ''})
        # old_data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        old_data = super().validate(attrs)
        data = {
            'msg': '登录成功',
            'id': self.user.id,
            'username': self.user.username,
            'admin': self.user.is_superuser,
            'refresh': old_data['refresh'],
            'token': old_data['access']
        }
        return data

class MyRefreshTokenSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        old_data = super().validate(attrs)
        data = {
            'token': old_data['access']
        }
        return data