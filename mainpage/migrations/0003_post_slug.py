# Generated by Django 3.1.3 on 2020-12-02 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20201202_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
