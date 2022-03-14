# Generated by Django 3.2.7 on 2022-03-12 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0046_info_established_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slideshow',
            options={'verbose_name': 'اسلاید شو', 'verbose_name_plural': 'مجموعه اسلاید شو'},
        ),
        migrations.AlterField(
            model_name='galery',
            name='is_video',
            field=models.BooleanField(default=False, editable=False, verbose_name='فرمت ویدئو دارد ؟'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_video',
            field=models.BooleanField(default=False, editable=False, verbose_name='فرمت ویدئو دارد ؟'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='content_type',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='is_video',
            field=models.BooleanField(default=False, editable=False, verbose_name='فرمت ویدئو دارد ؟'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='media',
            field=models.FileField(blank=True, editable=False, upload_to='slideshow'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name='آیدی محتوا'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='organ_id',
            field=models.PositiveBigIntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='organ_type',
            field=models.CharField(blank=True, editable=False, max_length=2),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='title',
            field=models.TextField(verbose_name='عنوان محتوا'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='type',
            field=models.TextField(verbose_name='نوع محتوا'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='video_poster',
            field=models.ImageField(blank=True, editable=False, upload_to='slideshow/poster'),
        ),
    ]