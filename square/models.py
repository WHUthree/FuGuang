from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

from user.models import User

type_choice = (
        (1, "中餐"), (2, "火锅"), (3, "烧烤"),
        (4, "西餐"), (5, "韩料"), (6, "日料"),
        (7, "甜品"), (8, "其它")
    )

class MealInfo(models.Model):
    title = models.CharField(max_length=20, verbose_name=u"标题")
    content = models.TextField(verbose_name="详情")
    member_num = models.IntegerField(validators=[MinValueValidator(2, message="至少两人约饭")],
                                     verbose_name="约饭总人数")
    grade_choice = (
        (1, "大一"), (2, "大二"), (3, "大三"), (4, "大四"),
        (5, "研一"), (6, "研二"), (7, "研三"),
        (8, "博一"), (9, "博二"), (10, "博三"), (11, "博四")
    )
    grade = models.MultiSelectField(choices=grade_choice, verbose_name="期望年级")
    location = models.CharField(max_length=30, verbose_name=u"地点")

    type = models.SmallIntegerField(choices=type_choice, verbose_name="种类")
    spicy_choice = (
        (1, "不辣"), (2, "微辣"),
        (3, "中辣"), (4, "重辣")
    )
    spicy = models.SmallIntegerField(choices=spicy_choice, verbose_name=u"辣度")
    cost = models.SmallIntegerField(validators=[MinValueValidator(0)], verbose_name="预期人均消费")

    end_time = models.DateTimeField(verbose_name=u"招募截止时间")
    dinner_time = models.DateTimeField(verbose_name=u"用餐时间")

    image1 = models.ImageField(null=True, blank=True, verbose_name="图片1")
    image2 = models.ImageField(null=True, blank=True, verbose_name="图片2")
    image3 = models.ImageField(null=True, blank=True, verbose_name="图片3")

    participants = models.ManyToManyField(User, related_name='meal_infos')
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="发布者")

    joined_num = models.IntegerField(default=0, verbose_name="已应募人数")
    is_complete = models.BooleanField(default=False, verbose_name=u"是否完成")
    class Meta:
        verbose_name = "约饭信息"
        verbose_name_plural = verbose_name


class LeftMessage(models.Model):
    meal = models.ForeignKey(MealInfo, on_delete=models.CASCADE, verbose_name=u"对应约饭记录")
    content = models.TextField(verbose_name=u"内容")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"留言者")

    class Meta:
        verbose_name = "留言"
        verbose_name_plural = verbose_name

class Appraise(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="被评价者")
    star = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="星数")
    class Meta:
        verbose_name = "评价"
        verbose_name_plural = verbose_name


class Share(models.Model):
    content = models.TextField(verbose_name="内容")
    cost = models.SmallIntegerField(validators=[MinValueValidator(0)], verbose_name="人均消费")
    location = models.CharField(max_length=30, verbose_name="地点")
    type = models.SmallIntegerField(choices=type_choice, verbose_name="种类")
    image1 = models.ImageField(null=True, blank=True, verbose_name="图片1")
    image2 = models.ImageField(null=True, blank=True, verbose_name="图片2")
    image3 = models.ImageField(null=True, blank=True, verbose_name="图片3")
    likes = models.SmallIntegerField(default=0, verbose_name="点赞数")

    post_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="发布者")
    class Meta:
        verbose_name = "分享"
        verbose_name_plural = verbose_name
