from django.shortcuts import render
from .models import WeatherData
from django.http import HttpResponse
# Create your views here.
def give_mean_temperature(request):
    all_weather_objects = WeatherData.objects.all()
    sum_of_temperature = 0
    count_of_temperatures = 0

    for record in all_weather_objects:
        sum_of_temperature += record.temperature
        count_of_temperatures += 1

    return HttpResponse(sum_of_temperature/count_of_temperatures)


def index(request):
    return render(request, "index.html",{} )


