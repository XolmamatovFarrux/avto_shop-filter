from django.urls import path

from avtoapp import views

urlpatterns = [
    path('car/', views.cars, name='cars'),
#     path('cars/', views.car, name='cars'),
  ]