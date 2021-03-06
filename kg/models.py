from django.db import models

#Create your models here.
#Temperatuur
#Ohuniiskus
#Tuuletugevus m/s
#Tuulesund (Pohi, Louna, Ida, Laas)

WIND_DIRECTION_CHOICES = (("North","NORTH"),
                          ("South","SOUTH"),
                          ("East","EAST"),
                          ("West", "WEST")
                          )

class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_strenght = models.IntegerField()
    wind_direction = models.CharField(choices=WIND_DIRECTION_CHOICES, max_length=5)
    date_of_record = models.DateTimeField(auto_now=True)


