# Generated by Django 2.1.7 on 2019-05-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ponto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='ip',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
