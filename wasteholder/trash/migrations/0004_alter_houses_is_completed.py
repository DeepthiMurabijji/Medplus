# Generated by Django 4.0.3 on 2022-05-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0003_houses_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='is_completed',
            field=models.CharField(default='Not Completed', max_length=50),
        ),
    ]