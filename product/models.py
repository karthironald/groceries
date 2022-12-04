from django.db import models
from groceries import enum

class TimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Category(TimeMixin):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

class Product(TimeMixin):
    name = models.CharField(max_length=200, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField(blank=False, null=False, default=1, help_text='Give the quantity of the product. Example, 1 kg, 2 litres, etc.')
    unit = models.CharField(max_length=100, choices=enum.MeasuringUnits.choices, blank=False, null=False, default='nos', help_text='Enter unit to measure the quantity. Example, 1kg, 2litre. Here, kg and litre are the units')
    cost = models.FloatField(blank=True, null=True, default=0.0)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.quantity:g} {self.unit.lower()})"

