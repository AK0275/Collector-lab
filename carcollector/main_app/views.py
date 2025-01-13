from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car, Service
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import CheckingForm

class CarCreate(CreateView):
    model = Car
    fields = ['name', 'model', 'description', 'price', 'image']


class CarUpdate(UpdateView):
    model= Car
    fields =['name', 'model', 'description', 'price', 'image']


class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'


class ServiceList(ListView):
    model = Service

class ServiceDetail(DetailView):
    model = Service

class ServiceCreate(CreateView):
    model = Service
    fields = '__all__'

class ServiceUpdate(UpdateView):
    model = Service
    fields = ['name']

class ServiceDelete(DeleteView):
    model = Service
    success_url = '/services/'



# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def car_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    checking_form = CheckingForm()
    services_car_doesnt_have = Service.objects.exclude(id__in = car.services.all().values_list('id'))
    return render(request, 'cars/detail.html', { 'car': car, 'checking_form': checking_form,
                                                'services': services_car_doesnt_have  })
    
    
def add_checking(request, car_id):
    form =CheckingForm(request.POST)
    if form.is_valid():
        new_checking = form.save(commit = False)
        new_checking.car_id = car_id
        new_checking.save()
        return redirect('detail', car_id = car_id)

def assoc_service(request, car_id, service_id):
    Car.objects.get(id=car_id).services.add(service_id)
    return redirect('detail', car_id = car_id)



def unassoc_service(request, car_id, service_id):
    Car.objects.get(id=car_id).services.remove(service_id)
    return redirect('detail', car_id = car_id)


