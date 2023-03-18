# Generated by Django 4.1.5 on 2023-02-28 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farming_app', '0009_feedback_model_alter_farmercomplain_model_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmercomplain_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 28, 18, 1, 40, 400960)),
        ),
        migrations.AlterField(
            model_name='farmertips_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 28, 18, 1, 40, 402026)),
        ),
        migrations.AlterField(
            model_name='feedback_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 28, 18, 1, 40, 402026)),
        ),
        migrations.AlterField(
            model_name='retailer_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 28, 18, 1, 40, 400960)),
        ),
        migrations.AlterField(
            model_name='retailer_model',
            name='crop_file',
            field=models.FileField(blank=True, upload_to='static/upload'),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 28, 18, 1, 40, 400960)),
        ),
    ]