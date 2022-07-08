from django.urls import path
from rest_framework import routers

from invoices.viewsets import InvoiceViewSet
from . import viewsets

router = routers.SimpleRouter()


router.register('invoice', InvoiceViewSet)

urlpatterns = router.urls + [
        path(
        'invoice/reservation/<int:reservation_id>',
        viewsets.invoice_reservation,
        name="detail-reservation-rooms"
    ),
]
