from django.db import models
from apps.catalog.models import Candy
from apps.production.models import ProductionBatch


class Sale(models.Model):
    order_number = models.CharField(max_length=40, unique=True)
    sold_at = models.DateTimeField()
    customer_name = models.CharField(max_length=120)

    def __str__(self):
        return self.order_number


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    candy = models.ForeignKey(Candy, on_delete=models.PROTECT)
    batch = models.ForeignKey(ProductionBatch, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_cost_snapshot = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.quantity * self.unit_price

    @property
    def cost_total(self):
        return self.quantity * self.unit_cost_snapshot

    @property
    def margin(self):
        return self.subtotal - self.cost_total
