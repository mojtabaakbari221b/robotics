# Generated by Django 3.2.7 on 2022-01-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220101_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='gallery/logo')),
            ],
        ),
        migrations.AddField(
            model_name='organ',
            name='galley',
            field=models.ManyToManyField(to='blog.Galery'),
        ),
        migrations.AddField(
            model_name='product',
            name='galley',
            field=models.ManyToManyField(to='blog.Galery'),
        ),
    ]
