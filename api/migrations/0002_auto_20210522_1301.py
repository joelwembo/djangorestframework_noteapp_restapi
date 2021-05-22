# Generated by Django 3.0.5 on 2021-05-22 05:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.CharField(default='joel wembo', max_length=100),
        ),
        migrations.AddField(
            model_name='note',
            name='date_field',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 5, 1, 20, 858910, tzinfo=utc), max_length=150),
        ),
        migrations.AddField(
            model_name='note',
            name='link',
            field=models.CharField(default='https:google.com', max_length=100),
        ),
        migrations.AddField(
            model_name='note',
            name='username',
            field=models.CharField(default='joelwembo', max_length=100),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
