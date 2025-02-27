from django.shortcuts import render, redirect

from avtoapp.forms import CarForm
from avtoapp.models import Car, Car_s


def cars(request):
    car = Car.objects.all()
    car_s = Car_s.objects.all()

    context = {
        'car': car,
        'car_s': car_s,

    }

    return render(request, 'cars.html', context=context)


def car_s(request,brand_id):
    car = Car.objects.all()
    car_s = Car_s.objects.filter(brand_id=brand_id)

    context = {
        'car_s': car_s,
        'car': car,
    }

    return render(request, 'test.html', context=context)


def info(request,car_s_id):
    car_s = Car_s.objects.get(pk=car_s_id)

    context = {
        'car_s': car_s,
    }

    return render(request, 'info.html', context=context)


def add_cars(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = Car.objects.create(**form.cleaned_data)
            return redirect('cars')
    else:
        form = CarForm()
    return render(request,'add_cars.html',{'form':form})
