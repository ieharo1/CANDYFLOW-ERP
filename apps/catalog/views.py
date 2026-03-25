from django.shortcuts import render
from apps.catalog.models import Candy


def candy_list(request):
    candies = Candy.objects.all().order_by('name')
    return render(request, 'catalog/candy_list.html', {'candies': candies})
