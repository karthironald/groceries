from django.db import models

class TimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Category(TimeMixin):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Product(TimeMixin):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name

