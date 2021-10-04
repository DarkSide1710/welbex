import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Welbex
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage


def main(request):
    welbex = Welbex.objects.all()
    number_of_item = 2

    paginator = Paginator(welbex, number_of_item)

    first_page = paginator.page(1).object_list
    # range of page ex range(1, 3)
    page_range = paginator.page_range

    context = {
        'paginator': paginator,
        'first_page': first_page,
        'page_range': page_range
    }
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None)  # getting page number
        results = list(paginator.page(page_n).object_list.values('id', 'name', 'quantity', 'distance', 'date'))
        return JsonResponse({"results": results})
    return render(request, 'crud_ajax/crud.html', context=context)


class CreateCrudWelbex(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        quantity1 = request.GET.get('quantity', None)
        distance1 = request.GET.get('distance', None)
        date1 = request.GET.get('date', None)

        obj = Welbex.objects.create(
            name=name1,
            quantity=quantity1,
            distance=distance1,
            date=date1,
        )

        welbex = {'id': obj.id, 'name': obj.name, 'quantity': obj.quantity, 'distance': obj.distance, 'date': obj.date}

        data = {
            'welbex': welbex
        }
        return JsonResponse(data)


class DeleteCrudWelbex(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Welbex.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudWelbex(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        quantity1 = request.GET.get('quantity', None)
        distance1 = request.GET.get('distance', None)

        obj = Welbex.objects.get(id=id1)
        obj.name = name1
        obj.quantity = quantity1
        obj.distance = distance1
        obj.date = datetime.date.today()
        print(obj.name)
        obj.save()
        welbex = {'id': obj.id, 'name': obj.name, 'quantity': obj.quantity, 'distance': obj.distance}

        data = {
            'welbex': welbex
        }
        return JsonResponse(data)
