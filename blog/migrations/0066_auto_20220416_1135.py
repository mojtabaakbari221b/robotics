# Generated by Django 3.2.7 on 2022-04-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0065_auto_20220416_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent',
            new_name='group',
        ),
    ]
