# Generated by Django 3.1.7 on 2021-04-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210413_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(help_text='Basligi daxil edin', max_length=200, unique=True, verbose_name='Xeber basligi'),
        ),
    ]