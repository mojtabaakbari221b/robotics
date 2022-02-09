# Generated by Django 3.2.7 on 2022-02-09 11:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_news_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='introduction_of_a_company',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='درباره شرکت'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='متن خبر'),
        ),
        migrations.AlterField(
            model_name='page',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='متنی که در صفحه قرار میگیرد'),
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='متن مرتبط به محصول'),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='متن نیازمندی'),
        ),
        migrations.AlterField(
            model_name='sitesupporter',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن مربوطه'),
        ),
        migrations.AlterField(
            model_name='standards',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن مرتبط به استاندارد'),
        ),
    ]