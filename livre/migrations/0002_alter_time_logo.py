# Generated by Django 3.2.6 on 2021-08-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='foto'),
        ),
    ]