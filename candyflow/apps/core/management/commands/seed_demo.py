from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.catalog.models import Candy
from apps.production.models import ProductionBatch, MaterialUsage
from apps.inventory.models import InventoryMovement
from apps.sales.models import Sale, SaleItem


class Command(BaseCommand):
    help = 'Carga datos demo de inicio a fin para CandyFlow.'

    def handle(self, *args, **options):
        if Candy.objects.exists():
            self.stdout.write(self.style.WARNING('Ya existen datos, se omite seed.'))
            return

        gummy = Candy.objects.create(name='Gomitas Mix', category='Gomitas', unit='bolsa', selling_price=Decimal('2.50'))
        lollipop = Candy.objects.create(name='Paleta Frutal', category='Paletas', unit='unidad', selling_price=Decimal('0.80'))

        batch1 = ProductionBatch.objects.create(
            code='LOT-2026-001', candy=gummy, production_date=timezone.now().date(),
            quantity_produced=Decimal('500'), labor_cost=Decimal('120'), overhead_cost=Decimal('80')
        )
        MaterialUsage.objects.create(batch=batch1, material_name='Gelatina', quantity=Decimal('30'), unit_cost=Decimal('3.0'))
        MaterialUsage.objects.create(batch=batch1, material_name='Azúcar', quantity=Decimal('50'), unit_cost=Decimal('1.2'))

        batch2 = ProductionBatch.objects.create(
            code='LOT-2026-002', candy=lollipop, production_date=timezone.now().date(),
            quantity_produced=Decimal('1000'), labor_cost=Decimal('90'), overhead_cost=Decimal('70')
        )
        MaterialUsage.objects.create(batch=batch2, material_name='Jarabe', quantity=Decimal('40'), unit_cost=Decimal('1.9'))

        InventoryMovement.objects.create(candy=gummy, batch=batch1, movement_type='IN', quantity=Decimal('500'), note='Entrada producción')
        InventoryMovement.objects.create(candy=lollipop, batch=batch2, movement_type='IN', quantity=Decimal('1000'), note='Entrada producción')

        sale = Sale.objects.create(order_number='VTA-1001', sold_at=timezone.now(), customer_name='Tienda Centro')
        SaleItem.objects.create(sale=sale, candy=gummy, batch=batch1, quantity=Decimal('120'), unit_price=Decimal('2.50'), unit_cost_snapshot=batch1.unit_cost)
        SaleItem.objects.create(sale=sale, candy=lollipop, batch=batch2, quantity=Decimal('300'), unit_price=Decimal('0.80'), unit_cost_snapshot=batch2.unit_cost)

        InventoryMovement.objects.create(candy=gummy, batch=batch1, movement_type='OUT', quantity=Decimal('120'), note='Salida por venta VTA-1001')
        InventoryMovement.objects.create(candy=lollipop, batch=batch2, movement_type='OUT', quantity=Decimal('300'), note='Salida por venta VTA-1001')

        self.stdout.write(self.style.SUCCESS('Seed demo cargado.'))
