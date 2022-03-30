# Generated by Django 3.2.7 on 2022-03-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0054_alter_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirements',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='requirements',
            name='fax',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requirements',
            name='phone',
            field=models.TextField(blank=True, null=True),
        ),
    ]
