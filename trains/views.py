from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from trains.models import Train
# from trains.forms import TrainForm

__all__ = (
    'home',
    'TrainDetailView',
    # 'TrainCreateView',
    # 'TrainUpdateView',
    # 'Train_delete'
)

from django.urls import reverse_lazy

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


def home(request):
    # if request.method == 'POST':
    #     form = TrainForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()
    # form = TrainForm()
    qs = Train.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'trains/home.html', context)

class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'
#
# class TrainCreateView(SuccessMessageMixin, CreateView):
#     model = Train
#     form_class = TrainForm
#     template_name = 'trains/create.html'
#     success_url = reverse_lazy('trains:home')
#     success_message = "Город успешно создан"
#
# class TrainUpdateView(SuccessMessageMixin, UpdateView):
#     model = Train
#     form_class = TrainForm
#     template_name = 'trains/update.html'
#     success_url = reverse_lazy('trains:home')
#     success_message = "Город успешно отредактирован"
#
# # class TrainDeleteView(DeleteView):
# #     model = Train
# #     success_url = reverse_lazy('trains:home')
# #
# #     def get(self, *args, **kwargs):
# #         return self.post(*args, **kwargs)
#
# def Train_delete(request, pk):
#     Train = get_object_or_404(Train, id=pk)
#     Train.delete()
#     form = TrainForm()
#     qs = Train.objects.all()
#     lst = Paginator(qs, 2)
#     page_number = request.GET.get('page')
#     page_obj = lst.get_page(page_number)
#     context = {'page_obj': page_obj, 'form': TrainForm}
#     return render(request, 'trains/home.html', context)