from django.db import models
from apps.catalog.models import Candy
from apps.production.models import ProductionBatch


class InventoryMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN', 'Entrada'),
        ('OUT', 'Salida'),
    ]
    candy = models.ForeignKey(Candy, on_delete=models.PROTECT)
    batch = models.ForeignKey(ProductionBatch, null=True, blank=True, on_delete=models.SET_NULL)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.candy.name} {self.movement_type} {self.quantity}'
