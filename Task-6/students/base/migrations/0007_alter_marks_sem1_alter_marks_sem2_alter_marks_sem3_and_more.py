# Generated by Django 4.0.3 on 2022-04-14 07:43

import base.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_st_details_phoneno_alter_st_details_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='sem1',
            field=models.FloatField(blank=True, null=True, validators=[base.models.validate_interval]),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sem2',
            field=models.FloatField(blank=True, null=True, validators=[base.models.validate_interval]),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sem3',
            field=models.FloatField(blank=True, null=True, validators=[base.models.validate_interval]),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sem4',
            field=models.FloatField(blank=True, null=True, validators=[base.models.validate_interval]),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sem5',
            field=models.FloatField(blank=True, null=True, validators=[base.models.validate_interval]),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sem6',
            field=models.FloatField(blank=True, null=True, validators=[base.models.validate_interval]),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sem7',
            field=models.FloatField(blank=True, null=True, validators=[base.models.validate_interval]),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sem8',
            field=models.FloatField(blank=True, null=True, validators=[base.models.validate_interval]),
        ),
        migrations.AlterField(
            model_name='st_details',
            name='phoneno',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]