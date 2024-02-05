from django.db import models
from User.models import User
class Recruit_Message(models.Model):
    volume = models.CharField(Max_length=3,verbose_name=u"就餐人数")
    grade = models.CharField(Max_length=3,verbose_name=u"年级")
    end_time = models.DateTimeField(verbose_name=u"招募截止时间")
    dinner_time = models.DateTimeField(verbose_name=u"用餐时间")
    form = models.CharField(Max_length=20,verbose_name=u"样式")
    taste = models.CharField(Max_length=20,verbose_name=u"口味")
    image = models.ImageField(upload_to='images/')

    user = models.ManyToManyField(User,related_name='recruit_message')