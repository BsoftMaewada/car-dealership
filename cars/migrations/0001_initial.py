# Generated by Django 3.2.9 on 2021-11-16 04:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField(choices=[(2021, 2021)], verbose_name='year')),
                ('condition', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('car_photo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('car_photo_1', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('car_photo_5', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('features', models.CharField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=255)),
                ('body_style', models.CharField(max_length=255)),
                ('engine', models.CharField(max_length=255)),
                ('transmission', models.CharField(max_length=255)),
                ('interior', models.CharField(max_length=255)),
                ('mileage', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=255)),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=100)),
                ('no_of_owners', models.CharField(max_length=255)),
                ('is_feature', models.BooleanField(max_length=255)),
                ('vin', models.CharField(max_length=255)),
                ('created_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]