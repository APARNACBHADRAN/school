# Generated by Django 4.2.2 on 2023-09-11 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_alter_departments_options_departments_d_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='departments',
        ),
    ]