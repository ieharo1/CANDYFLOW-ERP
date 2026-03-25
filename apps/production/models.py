from django.db import models
from apps.catalog.models import Candy


class ProductionBatch(models.Model):
    code = models.CharField(max_length=40, unique=True)
    candy = models.ForeignKey(Candy, on_delete=models.PROTECT)
    production_date = models.DateField()
    quantity_produced = models.DecimalField(max_digits=10, decimal_places=2)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    overhead_cost = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_material_cost(self):
        return sum(item.total_cost for item in self.material_items.all())

    @property
    def total_cost(self):
        return self.total_material_cost + self.labor_cost + self.overhead_cost

    @property
    def unit_cost(self):
        if self.quantity_produced == 0:
            return 0
        return self.total_cost / self.quantity_produced

    def __str__(self):
        return self.code


class MaterialUsage(models.Model):
    batch = models.ForeignKey(ProductionBatch, related_name='material_items', on_delete=models.CASCADE)
    material_name = models.CharField(max_length=120)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_cost(self):
        return self.quantity * self.unit_cost

    def __str__(self):
        return f'{self.material_name} - {self.batch.code}'
