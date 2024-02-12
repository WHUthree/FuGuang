from django.db import models


class user(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"名称")
    id = models.CharField(max_length=20, verbose_name=u"学号", primary_key=True)
    password = models.CharField(max_length=255, verbose_name=u"密码")
    phone_number = models.CharField(max_length=20, verbose_name=u"电话")

    # avatar = models.CharField(max_length=255,verbose_name=u"头像路径")

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
