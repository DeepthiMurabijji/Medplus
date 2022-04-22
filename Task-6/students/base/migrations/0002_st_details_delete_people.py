# Generated by Django 4.0.3 on 2022-04-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='st_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank='', max_length=45)),
                ('LastName', models.CharField(blank='', max_length=45)),
                ('rollno', models.CharField(blank='', help_text='Enter 4 digit roll number', max_length=4)),
                ('email', models.EmailField(blank='', max_length=265, unique=True)),
                ('phoneno', models.CharField(blank='', max_length=10)),
                ('Year', models.CharField(blank='', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=2)),
                ('Branch', models.CharField(blank='', choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('IT', 'IT')], max_length=3)),
                ('Section', models.CharField(blank='', choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='people',
        ),
    ]
