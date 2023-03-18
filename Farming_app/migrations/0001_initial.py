# Generated by Django 4.1.5 on 2023-02-23 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 23, 20, 57, 0, 606698))),
                ('authorised', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('number', models.BigIntegerField()),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]