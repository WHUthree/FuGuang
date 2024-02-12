from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class recruit_message(models.Model):
    #id = models.CharField(max_length=20, verbose_name=u"招募信息标识符", primary_key=True)
    title = models.CharField(max_length=20, verbose_name=u"标题")
    content = models.TextField(verbose_name="详情")
    member_num = models.IntegerField(validators=[MinValueValidator(2,message="至少两人约饭")],verbose_name="约饭总人数")
    grade_choice = (
        (1, "大一"), (2, "大二"), (3, "大三"), (4, "大四"),
        (5, "研一"), (6, "研二"), (7, "研三"),
        (8, "博一"), (9, "博二"), (10, "博三"), (11, "博四")
    )
    grade = models.SmallIntegerField(choices=grade_choice,verbose_name="年级")
    location = models.CharField(max_length=30, verbose_name=u"地点")

    type_choice = (
        (1, "中餐"), (2, "火锅"), (3, "烧烤"),
        (4, "西餐"), (5, "韩料"), (6, "日料"),
        (7, "甜品"), (8, "其它")
    )
    type = models.SmallIntegerField(choices=type_choice,verbose_name="种类")
    spicy_choice = (
        (1, "不辣"), (2, "微辣"), (3, "中辣"),
        (4, "重辣")
    )
    spicy = models.SmallIntegerField(choices=spicy_choice, verbose_name=u"辣度")
    end_time = models.DateTimeField(verbose_name=u"招募截止时间")
    dinner_time = models.DateTimeField(verbose_name=u"用餐时间")
    image = models.ImageField(upload_to='images/', verbose_name=u"美团店铺截图")
    is_complete = models.BooleanField(default=False, verbose_name=u"是否完成")
    participants = models.ManyToManyField('user.user', related_name='recruit_messages')
    class Meta:
        verbose_name = "招募信息"
        verbose_name_plural = verbose_name
class meal_record(models.Model):
    id = models.CharField(max_length=20, verbose_name=u"约饭记录标识符", primary_key=True)
    title = models.CharField(max_length=20, verbose_name=u"标题")
    dinner_time = models.DateTimeField(verbose_name=u"用餐时间")
    location = models.CharField(max_length=100, verbose_name=u"地点")
    image1 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="图片1")
    image2 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="图片2")
    image3 = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="图片3")
    likes = models.SmallIntegerField(default=0, verbose_name="点赞数")
    content = models.TextField(verbose_name=u"详情")
    post_user = models.ForeignKey('user.user', on_delete=models.CASCADE, verbose_name="发布者")

    class Meta:
        verbose_name = "约饭记录"
        verbose_name_plural = verbose_name
class Appraise(models.Model):
    recipient = models.ForeignKey('user.user', on_delete=models.CASCADE, verbose_name="被评价者")
    star = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="星数")
    class Meta:
        verbose_name = "评价信息"
        verbose_name_plural = verbose_name
