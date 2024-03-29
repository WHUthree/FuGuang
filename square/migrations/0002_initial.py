# Generated by Django 4.2.8 on 2024-02-13 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("square", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="share",
            name="post_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="发布者",
            ),
        ),
        migrations.AddField(
            model_name="recruit_message",
            name="participants",
            field=models.ManyToManyField(
                related_name="recruit_messages", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="recruit_message",
            name="post_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="发布者",
            ),
        ),
        migrations.AddField(
            model_name="mealinfo",
            name="participants",
            field=models.ManyToManyField(
                related_name="meal_records",
                to=settings.AUTH_USER_MODEL,
                verbose_name="约饭者",
            ),
        ),
        migrations.AddField(
            model_name="appraise",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="被评价者",
            ),
        ),
    ]
