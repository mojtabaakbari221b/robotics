# Generated by Django 3.2.7 on 2022-04-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0058_alter_tag_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(blank=True, max_length=4096, verbose_name='عنوان تگ'),
        ),
    ]