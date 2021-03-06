# Generated by Django 3.1.13 on 2021-10-22 19:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctoronlinemaster', '0013_auto_20211022_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctoronlinemaster.driver'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 19, 47, 14, 70527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 19, 47, 14, 70527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 22, 19, 47, 14, 69528, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 22, 19, 47, 14, 69528, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 47, 14, 71526)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 47, 14, 71526)),
        ),
        migrations.AlterField(
            model_name='patientmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 47, 14, 71526)),
        ),
        migrations.AlterField(
            model_name='specialistmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 47, 14, 72526)),
        ),
    ]
