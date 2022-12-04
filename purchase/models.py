from django.db import models
from product.models import TimeMixin, Product
from groceries import enum

class Store(TimeMixin):
    name = models.CharField(max_length=200, blank=False, null=False)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Purchase(TimeMixin):
    name = models.CharField(max_length=200, blank=True, null=True, default='New Purchase')
    purchased_at = models.DateTimeField(blank=False)
    cost = models.FloatField(blank=True, null=True, default=0.0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    comments = models.TextField(max_length=250, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.store})"

class PurchaseItem(TimeMixin):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False, default=1)
    cost = models.FloatField(blank=True, null=True, default=0.0)

    def __str__(self) -> str:
        return f"{self.purchase} ({self.product})"

    def total_quantity_string(self):
        t_quantity = self.product.quantity * self.quantity
        unit = self.product.unit
        if unit == enum.MeasuringUnits.GRAM:
            if t_quantity > 1000:
                t_quantity = t_quantity / 1000
                unit = enum.MeasuringUnits.KILOGRAM
            
        elif self.product.unit == enum.MeasuringUnits.MILLILITRE:
            if t_quantity > 1000:
                t_quantity = t_quantity / 1000
                unit = enum.MeasuringUnits.LITRE
        
        return f"{t_quantity:g} {unit}"