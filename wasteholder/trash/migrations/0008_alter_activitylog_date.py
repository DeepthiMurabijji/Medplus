# Generated by Django 4.0.3 on 2022-07-15 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0007_alter_activitylog_date_alter_activitylog_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='date',
            field=models.DateTimeField(db_column='Date', default=datetime.datetime(2022, 7, 15, 12, 13, 28, 927947)),
        ),
    ]
