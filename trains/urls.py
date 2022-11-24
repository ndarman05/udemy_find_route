from django.contrib import admin
from django.urls import path

from trains.views import *

app_name = 'trains'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    # path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    # # path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    # path('delete/<int:pk>/', city_delete, name='delete'),
    # path('add/', CityCreateView.as_view(), name='create'),
]



