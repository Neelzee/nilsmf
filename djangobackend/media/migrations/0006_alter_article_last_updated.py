# Generated by Django 4.2.1 on 2023-05-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_alter_article_body_media_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='last_updated',
            field=models.DateField(blank=True, null=True),
        ),
    ]
