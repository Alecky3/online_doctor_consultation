# Generated by Django 3.1.13 on 2021-10-23 12:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctoronlinemaster', '0015_auto_20211022_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 12, 50, 18, 494330, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 12, 50, 18, 494330, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driver',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='drivers_profile'),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 23, 12, 50, 18, 492332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 23, 12, 50, 18, 492332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 15, 50, 18, 495329)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 15, 50, 18, 495329)),
        ),
        migrations.AlterField(
            model_name='patientmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 15, 50, 18, 495329)),
        ),
        migrations.AlterField(
            model_name='specialistmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 15, 50, 18, 496329)),
        ),
        migrations.CreateModel(
            name='HomeCareServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=4, default=0.0, max_digits=20)),
                ('specialist', models.ManyToManyField(to='doctoronlinemaster.UserSpecialist')),
            ],
        ),
    ]