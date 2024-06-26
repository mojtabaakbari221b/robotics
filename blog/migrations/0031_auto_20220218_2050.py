# Generated by Django 3.2.7 on 2022-02-18 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_merge_0028_auto_20220218_1352_0029_auto_20220218_2039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='standards',
            options={'verbose_name': 'استاندارد', 'verbose_name_plural': 'استانداردها'},
        ),
        migrations.AlterField(
            model_name='galery',
            name='is_video',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_video',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='organ',
            name='standards',
            field=models.ManyToManyField(blank=True, related_name='organ_standards', to='blog.Standards', verbose_name='استاندارد ها'),
        ),
    ]
