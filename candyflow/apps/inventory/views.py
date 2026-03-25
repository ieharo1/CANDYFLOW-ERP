from django.shortcuts import render
from apps.inventory.models import InventoryMovement


def inventory_movements(request):
    movements = InventoryMovement.objects.select_related('candy', 'batch').order_by('-created_at')
    return render(request, 'inventory/movements.html', {'movements': movements})
