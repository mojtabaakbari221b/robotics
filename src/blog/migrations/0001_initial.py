# Generated by Django 3.2.7 on 2021-12-27 08:22

import ckeditor.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(max_length=256)),
                ('date_of_submission', models.DateField(default=django.utils.timezone.now)),
                ('text', ckeditor.fields.RichTextField(max_length=2056)),
                ('src', models.URLField(max_length=2056)),
                ('image', models.ImageField(upload_to='news/image')),
                ('media', models.FileField(upload_to='news/video')),
            ],
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', ckeditor.fields.RichTextField(max_length=256)),
                ('logo', models.ImageField(upload_to='organization/logo')),
                ('ceo_management_name', ckeditor.fields.RichTextField(max_length=128)),
                ('ceo_management_image', models.ImageField(upload_to='organization/ceo_logo')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('info', ckeditor.fields.RichTextField(max_length=512)),
                ('activity_type', ckeditor.fields.RichTextField(max_length=256)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1024), size=None)),
                ('type', models.CharField(choices=[('CO', 'Company'), ('LB', 'Labs')], default='CO', max_length=2)),
                ('category', models.ManyToManyField(to='blog.Category')),
                ('group', models.ManyToManyField(to='blog.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(max_length=256)),
                ('text', ckeditor.fields.RichTextField(max_length=2056)),
                ('applicant_entity_name', ckeditor.fields.RichTextField(max_length=256)),
                ('applicant_entity_logo', models.ImageField(upload_to='requirements/applicant_entity_image')),
                ('image', models.ImageField(upload_to='requirements/image')),
                ('date_of_submission', models.DateField(default=django.utils.timezone.now)),
                ('deadline', models.DateField()),
                ('file', models.FileField(upload_to='requirements/file')),
            ],
        ),
        migrations.CreateModel(
            name='Standards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(max_length=128)),
                ('image', models.ImageField(upload_to='standard/image')),
                ('text', ckeditor.fields.RichTextField(max_length=128)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.organ')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', ckeditor.fields.RichTextField(max_length=256)),
                ('text', ckeditor.fields.RichTextField(max_length=2056)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='product/image')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1024), size=None)),
                ('category', models.ManyToManyField(to='blog.Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.organ')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', ckeditor.fields.RichTextField(max_length=1024)),
                ('website', models.URLField(max_length=512)),
                ('established_year', models.DateField()),
                ('validation_of_knowledge_base', models.BooleanField(default=False)),
                ('introduction_of_a_company', ckeditor.fields.RichTextField(max_length=2048)),
                ('number_of_staff', models.PositiveIntegerField(null=True)),
                ('file', models.FileField(upload_to='info/file')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_company', to='blog.organ')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_name', models.CharField(max_length=128)),
                ('interface_phone_number', models.CharField(max_length=18)),
                ('tel_channel', models.URLField(max_length=256)),
                ('fax', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=512)),
                ('phone_number', models.CharField(max_length=18)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.organ')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.group'),
        ),
    ]
