# Generated by Django 3.2.7 on 2022-03-01 11:57

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_auto_20220228_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='info',
            field=django_quill.fields.QuillField(verbose_name='اطلاعات'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=django_quill.fields.QuillField(verbose_name='متن خبر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=django_quill.fields.QuillField(verbose_name='متن مرتبط به محصول'),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='text',
            field=django_quill.fields.QuillField(verbose_name='متن نیازمندی'),
        ),
    ]
