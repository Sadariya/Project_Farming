# Generated by Django 4.1.5 on 2023-03-26 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farming_app', '0012_alter_contactus_model_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 26, 11, 59, 39, 385389)),
        ),
        migrations.AlterField(
            model_name='farmercomplain_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 26, 11, 59, 39, 385389)),
        ),
        migrations.AlterField(
            model_name='farmertips_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 26, 11, 59, 39, 385389)),
        ),
        migrations.AlterField(
            model_name='feedback_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 26, 11, 59, 39, 385389)),
        ),
        migrations.AlterField(
            model_name='retailer_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 26, 11, 59, 39, 384395)),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 26, 11, 59, 39, 384395)),
        ),
    ]
