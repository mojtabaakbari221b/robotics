# Generated by Django 3.2.7 on 2022-02-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_organ_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_video',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='is_video',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='galery',
            name='is_video',
            field=models.BooleanField(default=False),
        ),
    ]
