# Generated by Django 3.1.3 on 2020-12-03 21:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20201203_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organism',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='creationdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 21, 34, 18, 438491, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updatedate',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 21, 34, 18, 438517, tzinfo=utc), verbose_name='date updated'),
        ),
    ]
