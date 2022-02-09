# Generated by Django 3.2.7 on 2022-02-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_slideshow_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='files',
            field=models.ManyToManyField(blank=True, to='blog.File', verbose_name='فایل ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gallery',
            field=models.ManyToManyField(blank=True, to='blog.Galery', verbose_name='گالری'),
        ),
        migrations.AlterField(
            model_name='product',
            name='standard',
            field=models.ManyToManyField(blank=True, to='blog.Standards', verbose_name='استاندارد ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='تگ ها'),
        ),
    ]
