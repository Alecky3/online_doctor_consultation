# Generated by Django 3.1.13 on 2021-10-22 19:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctoronlinemaster', '0012_auto_20211013_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(default='myemail@gmail.com', max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 19, 45, 6, 830185, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 19, 45, 6, 830185, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 22, 19, 45, 6, 828186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='homecare',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 22, 19, 45, 6, 828186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 45, 6, 830185)),
        ),
        migrations.AlterField(
            model_name='patientappointments',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 45, 6, 830185)),
        ),
        migrations.AlterField(
            model_name='patientmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 45, 6, 831185)),
        ),
        migrations.AlterField(
            model_name='specialistmessages',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 45, 6, 831185)),
        ),
    ]
