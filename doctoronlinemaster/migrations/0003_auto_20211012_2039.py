# Generated by Django 3.1.13 on 2021-10-12 17:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctoronlinemaster', '0002_auto_20211012_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='appointment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctoronlinemaster.userpatient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
