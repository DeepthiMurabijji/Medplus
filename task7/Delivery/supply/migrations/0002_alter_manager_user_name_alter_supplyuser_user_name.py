# Generated by Django 4.0.4 on 2022-05-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='user_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='supplyuser',
            name='user_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]