from django.db import models
from User.models import User
class Recruit_Message(models.Model):
    id = models.CharField(Max_length=20,null=False,blank=False,verbose_name=u"招募信息标识符")
    title = models.CharField(Max_length=20,null=False,blank=False,verbose_name=u"标题")
    volume = models.CharField(Max_length=3,null=False,blank=False,verbose_name=u"就餐人数")
    grade = models.CharField(Max_length=3,null=False,blank=False,verbose_name=u"年级")
    create_time = models.DateTimeField(null=False,blank=False,verbose_name=u"招募开始时间")
    end_time = models.DateTimeField(null=False,blank=False,verbose_name=u"招募截止时间")
    dinner_time = models.DateTimeField(null=False,blank=False,verbose_name=u"用餐时间")
    update_time = models.DateTimeField(null=False,blank=False,verbose_name=u"更新时间")
    form = models.CharField(Max_length=20,null=False,blank=False,verbose_name=u"样式")
    taste = models.CharField(Max_length=20,null=False,blank=False,verbose_name=u"口味")
    image = models.ImageField(upload_to='images/',null=False,blank=False,verbose_name=u"美团店铺截图")
    is_complete = models.BooleanField(default=False,null=False,blank=False,verbose_name=u"是否完成")

    user = models.ManyToManyField(User,related_name='recruit_message')