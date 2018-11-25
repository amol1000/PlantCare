from django.http import HttpResponse
import random

def index(request):
    moistureValue = random.randint(1,101)
    return HttpResponse(moistureValue)

def get_plant_data(request):
    return HttpResponse("10")
