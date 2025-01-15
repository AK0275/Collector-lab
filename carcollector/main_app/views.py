from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car, Service
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import CheckingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['name', 'model', 'description', 'price', 'image']

    def form_valid(self, form):
        print("self.request.user", self.request.user)
        print("form", form)
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarUpdate(LoginRequiredMixin, UpdateView):
    model= Car
    fields =['name', 'model', 'description', 'price', 'image']


class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'


class ServiceList(LoginRequiredMixin, ListView):
    model = Service

class ServiceDetail(LoginRequiredMixin, DetailView):
    model = Service

class ServiceCreate(LoginRequiredMixin, CreateView):
    model = Service
    fields = '__all__'

class ServiceUpdate(LoginRequiredMixin, UpdateView):
    model = Service
    fields = ['name']

class ServiceDelete(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = '/services/'



# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def car_index(request):
    # cars = Car.objects.all()
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    checking_form = CheckingForm()
    services_car_doesnt_have = Service.objects.exclude(id__in = car.services.all().values_list('id'))
    return render(request, 'cars/detail.html', { 'car': car, 'checking_form': checking_form,
                                                'services': services_car_doesnt_have  })
    
@login_required
def add_checking(request, car_id):
    form =CheckingForm(request.POST)
    if form.is_valid():
        new_checking = form.save(commit = False)
        new_checking.car_id = car_id
        new_checking.save()
        return redirect('detail', car_id = car_id)

@login_required
def assoc_service(request, car_id, service_id):
    Car.objects.get(id=car_id).services.add(service_id)
    return redirect('detail', car_id = car_id)


@login_required
def unassoc_service(request, car_id, service_id):
    Car.objects.get(id=car_id).services.remove(service_id)
    return redirect('detail', car_id = car_id)


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Signup- Please try again later.'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

