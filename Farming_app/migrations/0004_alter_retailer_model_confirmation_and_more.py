# Generated by Django 4.1.5 on 2023-02-25 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farming_app', '0003_retailer_model_confirmation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer_model',
            name='confirmation',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='retailer_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 25, 19, 53, 23, 518290)),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 25, 19, 53, 23, 518290)),
        ),
    ]
