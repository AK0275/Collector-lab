from django.urls import path
# from .models import Car
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='index'),
    path('cars/<int:car_id>/', views.car_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_checking/', views.add_checking, name='add_checking'),

    path('services/', views.ServiceList.as_view(), name='services_index'),
    path('services/<int:pk>/', views.ServiceDetail.as_view(), name='services_detail'),
    path('services/create/', views.ServiceCreate.as_view(), name='services_create'),
    path('services/<int:pk>/update/', views.ServiceUpdate.as_view(), name='services_update'),
    path('services/<int:pk>/delete/', views.ServiceDelete.as_view(), name='services_delete'),

    path('cars/<int:car_id>/assoc_service/<int:service_id>/', views.assoc_service, name='assoc_service'),

    path('cars/<int:car_id>/unassoc_service/<int:service_id>/', views.unassoc_service, name='unassoc_service'),

    path('accounts/signup/', views.signup, name='signup'),

]

