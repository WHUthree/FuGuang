from django.db import models


class recruit_message(models.Model):
    id = models.CharField(max_length=20, null=False, blank=False, verbose_name=u"招募信息标识符", primary_key=True)
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name=u"标题")
    volume = models.CharField(max_length=3, null=False, blank=False, verbose_name=u"就餐人数")
    grade = models.CharField(max_length=3, null=False, blank=False, verbose_name=u"年级")
    create_time = models.DateTimeField(null=False, blank=False, verbose_name=u"招募开始时间")
    end_time = models.DateTimeField(null=False, blank=False, verbose_name=u"招募截止时间")
    dinner_time = models.DateTimeField(null=False, blank=False, verbose_name=u"用餐时间")
    update_time = models.DateTimeField(null=False, blank=False, verbose_name=u"更新时间")
    form = models.CharField(max_length=20, null=False, blank=False, verbose_name=u"样式")
    taste = models.CharField(max_length=20, null=False, blank=False, verbose_name=u"口味")
    location = models.CharField(max_length=100, null=False, blank=False, verbose_name=u"地点")
    content = models.TextField(verbose_name="详情")
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=u"美团店铺截图")
    is_complete = models.BooleanField(default=False, null=False, blank=False, verbose_name=u"是否完成")

    user = models.ManyToManyField('user.user', related_name='recruit_messages')


class meal_record:
    id = models.CharField(max_length=20, null=False, blank=False, verbose_name=u"约饭记录标识符", primary_key=True)
    title = models.CharField(max_length=20, null=False, blank=False, verbose_name=u"标题")
    dinner_time = models.DateTimeField(null=False, blank=False, verbose_name=u"用餐时间")
    location = models.CharField(max_length=100, null=False, blank=False, verbose_name=u"地点")
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=u"用餐照片")
    content = models.TextField(verbose_name=u"详情")

    user = models.ManyToManyField('user.user', related_name='meal_records')


class square(models.Model):
    recruit_message = models.ForeignKey('recruit_message', on_delete=models.CASCADE)
    meal_record = models.ForeignKey('meal_record', on_delete=models.CASCADE)
