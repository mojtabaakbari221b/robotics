# Generated by Django 3.2.7 on 2022-02-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_slideshow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organ',
            name='files',
            field=models.ManyToManyField(blank=True, to='blog.File', verbose_name='فایل ها'),
        ),
        migrations.AlterField(
            model_name='organ',
            name='media',
            field=models.ManyToManyField(blank=True, to='blog.Galery', verbose_name='گالری'),
        ),
        migrations.AlterField(
            model_name='organ',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='تگ ها'),
        ),
    ]
