# Generated by Django 3.2.6 on 2022-06-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livre', '0007_auto_20210827_1001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pontuar',
            options={'verbose_name': 'Time', 'verbose_name_plural': 'Tabelas'},
        ),
        migrations.AddField(
            model_name='jogo',
            name='gols_total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
