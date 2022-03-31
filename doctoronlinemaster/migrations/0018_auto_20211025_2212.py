# Generated by Django 3.1.13 on 2021-10-25 19:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctoronlinemaster', '0017_auto_20211025_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambulance_orders',
            name='start_time',
        ),
        migrations.AddField(
            model_name='ambulance_orders',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 22, 12, 31, 746275)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 19, 12, 31, 750273, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 19, 12, 31, 750273, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 25, 19, 12, 31, 747275, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 25, 19, 12, 31, 747275, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 22, 12, 31, 750273)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 22, 12, 31, 750273)),
        ),
        migrations.AlterField(
            model_name='patientmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 22, 12, 31, 751272)),
        ),
        migrations.AlterField(
            model_name='specialistmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 22, 12, 31, 751272)),
        ),
    ]