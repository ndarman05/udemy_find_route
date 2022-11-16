from django.shortcuts import render

from cities.models import City
from cities.forms import CityForm

__all__ = (
    'home',
    'CityDetailView',
    'CityCreateView'
)

from django.urls import reverse_lazy

from django.views.generic import DetailView, CreateView


def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = CityForm()
    qs = City.objects.all()
    context = {'objects_list':qs, 'form':CityForm}
    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')