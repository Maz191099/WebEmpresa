# Generated by Django 3.0.6 on 2020-05-24 04:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200523_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 4, 21, 9, 827545, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]