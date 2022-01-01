# Generated by Django 3.2.7 on 2021-12-27 12:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSupporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', ckeditor.fields.RichTextField(max_length=256)),
                ('text', ckeditor.fields.RichTextField(max_length=2056)),
                ('image', models.ImageField(upload_to='supporter/image')),
            ],
        ),
    ]
