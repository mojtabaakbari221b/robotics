# Generated by Django 3.2.7 on 2022-02-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_slideshow_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='files',
            field=models.ManyToManyField(blank=True, to='blog.File', verbose_name='فایل ها'),
        ),
    ]
