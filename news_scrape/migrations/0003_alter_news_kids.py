# Generated by Django 3.2.5 on 2021-07-28 05:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_scrape', '0002_auto_20210727_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='kids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]
