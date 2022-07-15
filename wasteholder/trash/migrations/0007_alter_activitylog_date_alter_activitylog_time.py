# Generated by Django 4.0.3 on 2022-07-15 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0006_activitylog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='date',
            field=models.DateTimeField(db_column='Date', default=datetime.date(2022, 7, 15)),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='time',
            field=models.CharField(db_column='Time', default='Pending', max_length=20),
        ),
    ]
