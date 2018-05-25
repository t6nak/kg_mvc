from django import forms


WIND_DIRECTION_CHOICES = ("NORTH", "SOUTH", "EAST", "WEST")

class WeatherData(forms.Form):
    temperature = forms.FloatField(required=True)
    humidity = forms.IntegerField(required=True)
    wind_strenght = forms.IntegerField(required=True)
    wind_direction = forms.CharField(required=True)
