# Generated by Django 3.2.13 on 2022-04-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usertoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
