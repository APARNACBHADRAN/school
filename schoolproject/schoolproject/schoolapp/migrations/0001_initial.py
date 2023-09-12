# Generated by Django 4.2.2 on 2023-09-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(choices=[('CS', 'COMPUTER SCIENCE'), ('C', 'COMMERCE'), ('E', 'ENGLISH'), ('M', 'MATHS'), ('S', 'SOCIAL SCIENCE')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('dob', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
                'ordering': ('name',),
            },
        ),
    ]