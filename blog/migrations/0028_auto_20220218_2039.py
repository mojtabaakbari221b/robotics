# Generated by Django 3.2.7 on 2022-02-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_info_company_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video_poster',
            field=models.ImageField(blank=True, help_text='این فیلد موقعی استفاده میشود که یک ویدئو بارگزاری میکنید', null=True, upload_to='gallery', verbose_name='پوستر ویدئو'),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='organ_type',
            field=models.CharField(blank=True, editable=False, max_length=2),
        ),
        migrations.AddField(
            model_name='slideshow',
            name='video_poster',
            field=models.ImageField(blank=True, editable=False, upload_to='slideshow/poster'),
        ),
    ]
