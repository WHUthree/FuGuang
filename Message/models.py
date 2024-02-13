from django.db import models
from user.models import User

# Create your models here.
class Message(models.Model):
    group = models.IntegerField(verbose_name='所属群聊')
    content = models.TextField(verbose_name="消息内容")
    sender = models.ForeignKey(to='User',to_field='username',verbose_name='发送者', on_delete=models.CASCADE)
    send_time = models.DateTimeField(auto_now=True,verbose_name='发送时间')
    class Meta:
        verbose_name = "群聊消息"
        verbose_name_plural = verbose_name