# Generated by Django 3.2.7 on 2022-02-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_info_company_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='standards',
            options={},
        ),
        migrations.RemoveField(
            model_name='standards',
            name='organ',
        ),
        migrations.AddField(
            model_name='organ',
            name='standards',
            field=models.ManyToManyField(blank=True, related_name='organ_standards', to='blog.Standards'),
        ),
    ]
