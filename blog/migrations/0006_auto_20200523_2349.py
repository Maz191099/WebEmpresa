# Generated by Django 3.0.6 on 2020-05-24 04:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200523_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 4, 49, 28, 565879, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]