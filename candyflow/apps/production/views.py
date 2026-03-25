from django.shortcuts import render
from apps.production.models import ProductionBatch


def production_list(request):
    batches = ProductionBatch.objects.all().order_by('-production_date')
    return render(request, 'production/production_list.html', {'batches': batches})
