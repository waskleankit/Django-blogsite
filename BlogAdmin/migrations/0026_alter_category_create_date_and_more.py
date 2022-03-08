# Generated by Django 4.0 on 2022-01-05 07:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAdmin', '0025_alter_category_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 7, 55, 23, 110539, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 7, 55, 23, 110553, tzinfo=utc), verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 7, 55, 23, 110168, tzinfo=utc), verbose_name='date published'),
        ),
    ]