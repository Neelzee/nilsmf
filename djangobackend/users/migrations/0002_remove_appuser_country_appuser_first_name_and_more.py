# Generated by Django 4.2.1 on 2023-05-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='country',
        ),
        migrations.AddField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(default='first_name', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(default='last_name', max_length=50),
            preserve_default=False,
        ),
    ]
