# Generated by Django 3.2.7 on 2022-04-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0059_alter_tag_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='blog.Category', verbose_name='دسته بندی محصول'),
        ),
    ]
