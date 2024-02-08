from django.db import models
#from Recruit_Message.models import Recruit_Message

class User(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,verbose_name=u"名称")
    stu_id = models.CharField(max_length=20,null=False,blank=False,verbose_name=u"学号")
    password = models.CharField(max_length=255, null=False,blank=False,verbose_name=u"密码")
    phone_number = models.CharField(max_length=20,null=False,blank=False,verbose_name=u"电话")
    #avatar = models.CharField(max_length=255,verbose_name=u"头像路径")

    #recruit_message = models.ManyToManyField(Recruit_Message,related_name='user')

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


