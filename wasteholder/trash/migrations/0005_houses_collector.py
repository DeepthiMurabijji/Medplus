# Generated by Django 4.0.3 on 2022-05-27 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0004_alter_houses_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='collector',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trash.collector'),
        ),
    ]
