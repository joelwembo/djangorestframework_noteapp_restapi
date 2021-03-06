# Generated by Django 3.0.5 on 2021-05-22 11:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210522_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('question', models.TextField()),
                ('solution1', models.TextField(default='none')),
                ('solution2', models.TextField(default='none')),
                ('postedby', models.CharField(default='admin', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='date_field',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 11, 12, 56, 495369, tzinfo=utc), max_length=150),
        ),
    ]
