# Generated by Django 3.1.13 on 2021-10-13 16:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctoronlinemaster', '0008_auto_20211013_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmenttypes',
            name='duration',
            field=models.TimeField(default=datetime.time(1, 0)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 16, 2, 44, 858512, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 16, 2, 44, 858512, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 16, 2, 44, 856514, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 16, 2, 44, 856514, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 19, 2, 44, 858512)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 19, 2, 44, 858512)),
        ),
    ]
