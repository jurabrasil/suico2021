# Generated by Django 3.2.6 on 2021-08-26 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livre', '0004_auto_20210820_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pontuar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('j', models.IntegerField()),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livre.time')),
            ],
        ),
    ]
