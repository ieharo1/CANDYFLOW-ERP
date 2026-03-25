from django.db import models


class Candy(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    unit = models.CharField(max_length=30, default='unidad')
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
