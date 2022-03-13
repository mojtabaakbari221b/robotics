# Generated by Django 3.2.7 on 2022-03-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_auto_20220312_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organ',
            name='type',
            field=models.CharField(choices=[('CO', 'Company'), ('LB', 'Labs'), ('SC', 'Services'), ('PR', 'Printer')], default='CO', max_length=2, verbose_name='نوع شرکت'),
        ),
    ]
