from django.shortcuts import render, redirect
from .forms import WeatherDataForm, WeatherData
from django.http import HttpResponse
from django.http import JsonResponse
from . import models

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
    if request.method == "POST":
        form = WeatherDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return redirect("index")

    elif request.method == "GET":
        weather_record_list = WeatherData.objects.all()
        form = WeatherDataForm()
        return render(request, "index.html", context={"form":form,
         "weather_records": weather_record_list
                                                      })








