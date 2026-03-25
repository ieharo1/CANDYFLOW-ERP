from decimal import Decimal
from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from django.shortcuts import render
from apps.production.models import ProductionBatch
from apps.sales.models import SaleItem
from apps.inventory.models import InventoryMovement


def dashboard(request):
    total_batches = ProductionBatch.objects.count()
    total_production_cost = sum((batch.total_cost for batch in ProductionBatch.objects.all()), Decimal('0'))

    revenue_expr = ExpressionWrapper(F('quantity') * F('unit_price'), output_field=DecimalField(max_digits=12, decimal_places=2))
    revenue = SaleItem.objects.aggregate(total=Sum(revenue_expr)).get('total') or Decimal('0')

    cost_expr = ExpressionWrapper(F('quantity') * F('unit_cost_snapshot'), output_field=DecimalField(max_digits=12, decimal_places=2))
    cogs = SaleItem.objects.aggregate(total=Sum(cost_expr)).get('total') or Decimal('0')

    stock = {}
    for movement in InventoryMovement.objects.select_related('candy').all():
        key = movement.candy.name
        stock.setdefault(key, Decimal('0'))
        if movement.movement_type == 'IN':
            stock[key] += movement.quantity
        else:
            stock[key] -= movement.quantity

    context = {
        'total_batches': total_batches,
        'total_production_cost': total_production_cost,
        'revenue': revenue,
        'cogs': cogs,
        'gross_profit': revenue - cogs,
        'inventory_balance': stock,
    }
    return render(request, 'core/dashboard.html', context)
