from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from cities.models import City
from cities.forms import CityForm

__all__ = (
    'home',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView',
)

from django.urls import reverse_lazy

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj':page_obj, 'form':CityForm}
    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Город успешно создан"

class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Город успешно отредактирован"

class CityDeleteView(DeleteView):
    model = City
    success_url = reverse_lazy('trains:home')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

# def city_delete(request, pk):
#     city = get_object_or_404(City, id=pk)
#     city.delete()
#     form = CityForm()
#     qs = City.objects.all()
#     lst = Paginator(qs, 2)
#     page_number = request.GET.get('page')
#     page_obj = lst.get_page(page_number)
#     context = {'page_obj': page_obj, 'form': CityForm}
#     return render(request, 'trains/home.html', context)