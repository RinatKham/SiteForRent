from django.shortcuts import render
from .models import CarModel, RentModel
from .forms import RentForm


def index(request):
    return render(request, 'rentcarsapp/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'rentcarsapp/about.html', {'title': 'О нас'})


def cars(request):
    carmodels = CarModel.objects.order_by('title')
    return render(request, 'rentcarsapp/cars.html', {'title': 'Каталог авто', 'carmodels': carmodels})

def rent(request):
    message = ''
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            message = 'Форма не корректна'
    form = RentForm()
    carmodels = CarModel.objects.order_by('title')
    context = {
        'form': form,
        'message': message,
        'title': 'Аренда авто',
        'carmodels': carmodels
    }
    carmodels = CarModel.objects.order_by('title')
    return render(request, 'rentcarsapp/rent.html', context)