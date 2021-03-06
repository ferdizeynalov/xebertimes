# Generated by Django 3.1.7 on 2021-04-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Basligi daxil edin', max_length=200, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='partners/%Y/%m/%d/')),
                ('site', models.URLField(editable=False)),
            ],
        ),
    ]
