from django.urls import path
from .views import PurchaseListView, PurchaseItemListView

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase-list'),
    path('<int:purchase_id>/items', PurchaseItemListView.as_view(), name='purchaseitem-list')
]