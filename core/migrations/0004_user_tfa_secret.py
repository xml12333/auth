# Generated by Django 3.2.13 on 2022-04-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_reset'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tfa_secret',
            field=models.CharField(default='', max_length=255),
        ),
    ]
