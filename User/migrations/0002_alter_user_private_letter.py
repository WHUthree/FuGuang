# Generated by Django 4.2 on 2024-02-06 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="private_letter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="User.privateletter",
                verbose_name="私信",
            ),
        ),
    ]