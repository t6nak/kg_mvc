
from kg.models import WeatherData
from django.forms import ModelForm


WIND_DIRECTION_CHOICES = (("North","NORTH"),
                          ("South","SOUTH"),
                          ("East","EAST"),
                          ("West", "WEST")
                          )

class WeatherDataForm(ModelForm):
    class Meta:
        model = WeatherData
        fields = ["temperature", "humidity", "wind_direction" ,"wind_strenght" ]
