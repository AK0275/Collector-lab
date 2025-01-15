from django.contrib import admin
from .models import Car, CHECKING, Service, Profile


# Register your models here.
admin.site.register(Car)
admin.site.register(CHECKING)
admin.site.register(Service)
admin.site.register(Profile)

