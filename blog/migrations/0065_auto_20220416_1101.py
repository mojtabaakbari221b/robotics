# Generated by Django 3.2.7 on 2022-04-16 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0064_auto_20220416_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='group',
        ),
        migrations.RemoveField(
            model_name='product',
            name='group',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='گروه'),
        ),
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
        migrations.DeleteModel(
            name='Group',
        ),
    ]
