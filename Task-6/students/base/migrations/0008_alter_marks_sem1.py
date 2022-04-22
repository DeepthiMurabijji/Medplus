# Generated by Django 4.0.3 on 2022-04-14 09:42

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_marks_sem1_alter_marks_sem2_alter_marks_sem3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='sem1',
            field=models.FloatField(blank=True, editable=False, null=True, validators=[base.models.validate_interval]),
        ),
    ]
