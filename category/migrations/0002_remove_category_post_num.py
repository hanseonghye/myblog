# Generated by Django 2.2.6 on 2019-11-03 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post_num',
        ),
    ]
