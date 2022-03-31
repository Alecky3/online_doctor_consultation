# Generated by Django 3.1.13 on 2021-10-13 16:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctoronlinemaster', '0011_auto_20211013_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmessages',
            name='type',
            field=models.CharField(default='New Appointment', max_length=255),
        ),
        migrations.AddField(
            model_name='specialistmessages',
            name='type',
            field=models.CharField(default='New Appointment', max_length=255),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 16, 58, 19, 457259, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 16, 58, 19, 457259, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 16, 58, 19, 455256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 16, 58, 19, 455256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 19, 58, 19, 457259)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 19, 58, 19, 457259)),
        ),
        migrations.AlterField(
            model_name='patientmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 19, 58, 19, 458258)),
        ),
        migrations.AlterField(
            model_name='specialistmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 19, 58, 19, 458258)),
        ),
    ]
