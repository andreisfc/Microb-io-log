# Generated by Django 3.1.3 on 2020-12-02 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_auto_20201202_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]