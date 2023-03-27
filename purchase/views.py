from django.views.generic.list import ListView
from .models import Purchase, PurchaseItem

class PurchaseListView(ListView):
    model = Purchase
    paginate_by: int = 50

class PurchaseItemListView(ListView):
    model = PurchaseItem
    paginate_by: int = 50