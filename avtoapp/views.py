from django.shortcuts import render

from avtoapp.models import Car, Car_s


def cars(request):
    car = Car.objects.filter()
    carl = Car_s.objects.filter()

    context = {
        'car': car,
        'car_s': carl,

    }

    return render(request, 'cars.html', context=context)


def index(request):
    car = Car.objects.all()
    carl = Car_s.objects.all()

    context = {
        'car': car,
        'car_s': carl,

    }

    return render(request, 'index.html', context=context)
