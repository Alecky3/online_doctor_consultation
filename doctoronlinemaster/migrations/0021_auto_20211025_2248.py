# Generated by Django 3.1.13 on 2021-10-25 19:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctoronlinemaster', '0020_auto_20211025_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homecareservices',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='homecareservices',
            name='patient',
        ),
        migrations.AddField(
            model_name='homecare',
            name='homecareservice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctoronlinemaster.homecareservices'),
        ),
        migrations.AlterField(
            model_name='ambulance_orders',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 19, 48, 8, 469060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 19, 48, 8, 469060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 25, 22, 48, 8, 466061)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 25, 22, 48, 8, 466061)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 22, 48, 8, 469060)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 22, 48, 8, 469060)),
        ),
        migrations.AlterField(
            model_name='patientmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 22, 48, 8, 470058)),
        ),
        migrations.AlterField(
            model_name='specialistmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 22, 48, 8, 470058)),
        ),
    ]
