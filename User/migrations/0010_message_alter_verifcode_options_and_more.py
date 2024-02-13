# Generated by Django 4.2 on 2024-02-13 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0009_alter_user_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="私信内容")),
                (
                    "timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="私信的发送时间"),
                ),
            ],
            options={
                "verbose_name": "用户私信表",
                "verbose_name_plural": "用户私信表",
                "db_table": "message",
            },
        ),
        migrations.AlterModelOptions(
            name="verifcode",
            options={"verbose_name": "手机验证码表", "verbose_name_plural": "手机验证码表"},
        ),
        migrations.RemoveField(
            model_name="user",
            name="private_letter",
        ),
        migrations.DeleteModel(
            name="PrivateLetter",
        ),
        migrations.AddField(
            model_name="message",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_messages",
                to=settings.AUTH_USER_MODEL,
                verbose_name="接收方",
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="sender",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sent_messages",
                to=settings.AUTH_USER_MODEL,
                verbose_name="发送方",
            ),
        ),
    ]