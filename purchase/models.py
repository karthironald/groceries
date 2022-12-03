from django.db import models
from product.models import Product, TimeMixin

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
    MEASURING_UNITS = [
        ('lt', 'litre'),
        ('kg', 'kgs'),
        ('g', 'g'),
        ('nos', 'nos'),
        ('pack', 'pack'),
        ('roll', 'roll'),
    ]

    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False, default=1)
    unit = models.CharField(max_length=100, choices=MEASURING_UNITS, blank=False, null=False, default='nos')
    cost = models.FloatField(blank=True, null=True, default=0.0)

    def __str__(self) -> str:
        return f"{self.purchase} ({self.product})"