from django.urls import path

from avtoapp import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('car_s/<int:brand_id>/',views.car_s, name='car_s'),
    path('info/<int:car_s_id>/', views.info, name='info'),
    path('add_cars/',views.add_cars, name='add_cars'),
  ]