# Generated by Django 2.2.4 on 2020-07-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keltrans_app', '0003_remove_user_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='packet',
            field=models.FileField(upload_to='carriers/packets'),
        ),
    ]
