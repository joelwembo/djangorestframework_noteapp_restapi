# Generated by Django 3.2.8 on 2021-10-20 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210522_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_field',
            field=models.DateField(default=django.utils.timezone.now, max_length=150),
        ),
    ]