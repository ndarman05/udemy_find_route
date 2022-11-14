from django.shortcuts import render

from cities.models import City

__all__ = (
    'home',
)

# Create your views here.
def home(request, pk=None):
    if pk:
        city = City.objects.filter(id=pk).first()
        context = {'object':city}
        return render(request, 'cities/detail.html', context)
    qs = City.objects.all()
    context = {'objects_list':qs}
    return render(request, 'cities/home.html', context)