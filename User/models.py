from django.db import models
from common.db import BaseModel
from django.contrib.auth.models import AbstractUser

class PrivateLetter(models.Model):
    """私信模型"""
    pass


class GenderType(models.IntegerChoices):
    """
    性别，主要用于用户表
    """

    UNKNOWN = 0, "未知"
    MALE = 1, "男"
    FEMALE = 2, "女"



class User(AbstractUser, BaseModel):

    # 基本信息
    username = models.CharField(max_length=20, unique=True, verbose_name="用户名")
    wechat = models.CharField(max_length=25, default="", verbose_name="wechat")
    student_number = models.CharField(max_length=20, verbose_name="学号")
    phone_number = models.CharField(max_length=20, verbose_name="电话")
    grade = models.IntegerField(default=0, verbose_name="年级")
    email = models.CharField(max_length=20, verbose_name="邮箱", null=True, blank=True)

    # 个性化
    avatar = models.ImageField(verbose_name="用户头像", blank=True, null=True)
    gender = models.IntegerField(
        choices=GenderType.choices,
        default=GenderType.UNKNOWN,
        verbose_name="性别",
    )


    #  权限认证
    is_authenticated = models.BooleanField("是否激活", default=True)
    is_staff = models.BooleanField("管理员", default=False)
    is_superuser = models.BooleanField("超级用户", default=False)
    password = models.CharField(max_length=150, null=True, blank=True, verbose_name="密码")
    openid = models.CharField(
        max_length=64,
        unique=True,
        null=True,
        verbose_name="微信openid"
    )


    #  私信功能
    private_letter = models.ForeignKey(
        PrivateLetter,
        on_delete=models.CASCADE,
        verbose_name='私信',
        null=True,
        blank=True)

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        app_label = "User"
        db_table = "users"




class VerifCode(models.Model):
    """验证码模型"""
    phone_number = models.CharField(verbose_name="手机号码", max_length=11)
    code = models.CharField(max_length=6, verbose_name="验证码")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="生成时间")
    class Meta:
        verbose_name = "手机验证码表"
        db_table = 'verifcode'
