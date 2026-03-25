from django.shortcuts import render
from apps.sales.models import Sale


def sale_list(request):
    sales = Sale.objects.prefetch_related('items__candy').order_by('-sold_at')
    return render(request, 'sales/sale_list.html', {'sales': sales})
