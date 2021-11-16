from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
#car_title
# city
# state
# color
# model
# year
# condition
# price
# description
# car_photo_1
# car_photo_2
# car_photo_3
# car_photo_4
# car_photo_5
# features
# body_style
# engine
# transmission
# interior
# mileage
# fuel_type
# no_of_owners
# created_date

class Car(models.Model):
    state_choices = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    # To auto populate the year from 2021 above
    year_choice =[]
    for i in range(2000, (datetime.now().year + 1)):
        year_choice.append((i, i))
        
        features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    
    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choices, max_length=255)
    city = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(('year'), choices = year_choice)
    condition = models.CharField(max_length=255)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    car_photo_5 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    doors = models.CharField(choices=door_choices, max_length=10)
    no_of_owners = models.CharField(max_length=255)
    is_feature = models.BooleanField(default=False)
    vin = models.CharField(max_length=255)
    created_date = models.DateField(default=datetime.now, blank=True)
    

