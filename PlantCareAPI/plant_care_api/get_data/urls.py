from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/get_plant_data', views.get_plant_data, name='get_plant_data'),
]
