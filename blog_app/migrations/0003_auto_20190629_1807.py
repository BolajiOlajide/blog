# Generated by Django 2.2.2 on 2019-06-29 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20190629_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
