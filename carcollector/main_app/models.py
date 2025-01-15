from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

CHECKS = (
    ('T', 'Tire'),
    ('B', 'Brakes'),
    ('L', 'Lights'),
    ('E', 'Engine Oil'),
    ('F', 'Fuel'),
)


class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('services_detail', kwargs={'pk': self.id})


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    services = models.ManyToManyField(Service)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


    def __str__(self):
        return self.name
    
    def checked_for_today(self):
        return self.checking_set.filter(date = date.today()).count() >= len(CHECKS)


class CHECKING(models.Model):
    date = models.DateField()
    chck = models.CharField(max_length=1, choices=CHECKS, default=CHECKS[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_chck_display()} on {self.date}"
    





class Meta:
    ordering = ['-date']