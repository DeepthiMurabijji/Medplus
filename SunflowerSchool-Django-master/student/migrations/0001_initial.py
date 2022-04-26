# Generated by Django 4.0.3 on 2022-04-06 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=50)),
                ('DOB', models.CharField(max_length=50)),
                ('parent_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('branch', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('java', models.CharField(max_length=50)),
                ('python', models.CharField(max_length=50)),
                ('sql', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]