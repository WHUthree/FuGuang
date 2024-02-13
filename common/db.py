import os

from django.db import models
from django.http import FileResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from fuguang.settings import MEDIA_ROOT


class BaseModel(models.Model):
    """公共字段"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="删除标记")

    class Meta:
        # 声明这是一张抽象模型，在执行迁移文件时不会在数据库中生成表
        abstract = True
        verbose_name = "公共字段表"
        verbose_name_plural = "公共字段表"
        db_table = "BaseTable"


# 获取文件公共接口
class FileView(APIView):
    def get(self, request, name):
        path = MEDIA_ROOT / name
        if os.path.isfile(path):
            return FileResponse(open(path, 'rb'))
        return Response({"error": "文件不存在"}, status=status.HTTP_404_NOT_FOUND)