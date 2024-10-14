from django.http import Http404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


from .models import Car, Sale


def cars_list_view(request):
    # получите список авто
    template_name = 'main/list.html'
    all_objects = Car.objects.all()
    context = {
        'cars': all_objects
    }
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    try:
        selected_car = Car.objects.get(id=car_id)
        context = {
            'car': selected_car
        }
        template_name = 'main/details.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except ObjectDoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        selected_car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=selected_car)
        context = {
            'car': selected_car,
            'sales': sales
        }
        template_name = 'main/sales.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except ObjectDoesNotExist:
        raise Http404('Car not found')
