# Generated by Django 2.1.7 on 2019-05-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ponto', '0002_auto_20190524_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='entrada1',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
