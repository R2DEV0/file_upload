# Generated by Django 2.2.4 on 2020-07-17 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keltrans_app', '0002_auto_20200717_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='home',
        ),
    ]
