# Generated by Django 4.2.4 on 2024-02-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('square', '0003_leftmessage_alter_appraise_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='post_time',
            field=models.DateTimeField(auto_now=True, verbose_name='分享时间'),
        ),
    ]