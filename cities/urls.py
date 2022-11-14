from django.contrib import admin
from django.urls import path

from cities.views import *

app_name = 'cities'

urlpatterns = [
    path('', home, name='home'),
]
