# Generated by Django 4.1.5 on 2023-02-24 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farming_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='retailer_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 24, 21, 43, 56, 44942))),
                ('option', models.CharField(max_length=15)),
                ('crop_name', models.CharField(max_length=50)),
                ('crop_about', models.CharField(max_length=150)),
                ('crop_file', models.FileField(upload_to='static/upload')),
                ('crop_quantity', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 24, 21, 43, 56, 43942)),
        ),
    ]
