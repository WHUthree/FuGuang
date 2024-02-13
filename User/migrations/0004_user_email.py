# Generated by Django 4.2 on 2024-02-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0003_alter_user_managers_remove_user_date_joined_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.CharField(
                blank=True, max_length=20, null=True, unique=True, verbose_name="邮箱"
            ),
        ),
    ]