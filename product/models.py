from django.db import models

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
    quantity = models.IntegerField(blank=False, null=False, default=1)
    unit = models.CharField(max_length=100, choices=MEASURING_UNITS, blank=False, null=False, default='nos')
    cost = models.FloatField(blank=True, null=True, default=0.0)
    
    def __str__(self) -> str:
        return self.name

