# Generated by Django 3.2.7 on 2022-02-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220209_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='type',
            field=models.TextField(),
        ),
    ]
