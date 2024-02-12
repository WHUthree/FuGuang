# Generated by Django 4.2.4 on 2024-02-12 14:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recruit_message',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='信息标识符')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('content', models.TextField(verbose_name='详情')),
                ('member_num', models.IntegerField(validators=[django.core.validators.MinValueValidator(2, message='至少两人约饭')], verbose_name='约饭总人数')),
                ('grade', models.SmallIntegerField(choices=[(1, '大一'), (2, '大二'), (3, '大三'), (4, '大四'), (5, '研一'), (6, '研二'), (7, '研三'), (8, '博一'), (9, '博二'), (10, '博三'), (11, '博四')], verbose_name='年级')),
                ('location', models.CharField(max_length=30, verbose_name='地点')),
                ('type', models.SmallIntegerField(choices=[(1, '中餐'), (2, '火锅'), (3, '烧烤'), (4, '西餐'), (5, '韩料'), (6, '日料'), (7, '甜品'), (8, '其它')], verbose_name='种类')),
                ('spicy', models.SmallIntegerField(choices=[(1, '不辣'), (2, '微辣'), (3, '中辣'), (4, '重辣')], verbose_name='辣度')),
                ('end_time', models.DateTimeField(verbose_name='招募截止时间')),
                ('dinner_time', models.DateTimeField(verbose_name='用餐时间')),
                ('image', models.ImageField(upload_to='images/', verbose_name='美团店铺截图')),
                ('is_complete', models.BooleanField(default=False, verbose_name='是否完成')),
                ('likes', models.SmallIntegerField(default=0, verbose_name='点赞数')),
                ('participants', models.ManyToManyField(related_name='recruit_messages', to='user.user')),
                ('post_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='发布者')),
            ],
            options={
                'verbose_name': '约饭记录',
                'verbose_name_plural': '约饭记录',
            },
        ),
        migrations.CreateModel(
            name='Appraise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='星数')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='被评价者')),
            ],
            options={
                'verbose_name': '评价信息',
                'verbose_name_plural': '评价信息',
            },
        ),
    ]