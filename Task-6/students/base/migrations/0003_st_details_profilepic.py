# Generated by Django 4.0.3 on 2022-04-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_st_details_delete_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='st_details',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
