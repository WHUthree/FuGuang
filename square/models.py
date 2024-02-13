from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from user.models import User

# Create your models here.

type_choice = (
        (1,"中餐"),(2,"火锅"),(3,"烧烤"),
        (4,"西餐"),(5,"韩料"),(6,"日料"),
        (7,"甜品"),(8,"其它")
    )
class MealInfo(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    content = models.TextField(verbose_name="详情")
    member_num = models.IntegerField(validators=[MinValueValidator(2,message="至少两人约饭")],verbose_name="约饭总人数")
    grade_choice = (
        (1,"大一"),(2,"大二"),(3,"大三"),(4,"大四"),
        (5,"研一"),(6,"研二"),(7,"研三"),
        (8, "博一"), (9, "博二"), (10, "博三"),(11,"博四")
    )
    grade = models.SmallIntegerField(choices=grade_choice,verbose_name="年级")
    location = models.CharField(max_length=30,verbose_name="位置")
    cost = models.SmallIntegerField(validators=[MinValueValidator(0,message="你倒贴请吃饭？")],verbose_name="人均消费")
    type = models.SmallIntegerField(choices=type_choice,verbose_name="种类")
    #口味?
    end_time = models.DateTimeField(verbose_name="招募截止时间")
    meal_time = models.DateTimeField(verbose_name="吃饭时间")
    image1 = models.ImageField(upload_to='images/',null=True,blank=True,verbose_name="图片1")
    image2 = models.ImageField(upload_to='images/',null=True,blank=True,verbose_name="图片2")
    image3 = models.ImageField(upload_to='images/',null=True,blank=True,verbose_name="图片3")

    participants = models.ManyToManyField(User,related_name="meal_records",verbose_name="约饭者")
    is_complete = models.BooleanField(default=False,verbose_name="是否完成")

    class Meta:
        verbose_name = "约饭信息"
        verbose_name_plural = verbose_name


class Appraise(models.Model):
    recipient = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="被评价者")
    star = models.SmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],verbose_name="星数")

    class Meta:
        verbose_name = "评价信息"
        verbose_name_plural = verbose_name


class Share(models.Model):
    content = models.TextField(verbose_name="内容")
    cost = models.SmallIntegerField(validators=[MinValueValidator(0, message="你倒贴请吃饭？")], verbose_name="人均消费")
    location = models.CharField(max_length=30, verbose_name="位置")
    type = models.SmallIntegerField(choices=type_choice,verbose_name="种类")
    image1 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="图片1")
    image2 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="图片2")
    image3 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="图片3")
    likes = models.SmallIntegerField(default=0,verbose_name="点赞数")

    post_user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="发布者")

    class Meta:
        verbose_name = "分享"
        verbose_name_plural = verbose_name
