# Generated by Django 4.2.4 on 2024-03-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_appraise_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='star',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=2, verbose_name='评价星数'),
        ),
    ]
