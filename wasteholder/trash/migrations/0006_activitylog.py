# Generated by Django 4.0.3 on 2022-07-14 12:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0005_houses_collector'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, db_column='Date', default=datetime.date(2022, 7, 14), null=True)),
                ('time', models.TimeField(blank=True, db_column='Time', null=True)),
                ('collector', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trash.collector')),
                ('houses', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trash.houses')),
            ],
        ),
    ]