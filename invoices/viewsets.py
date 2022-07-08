from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from reservations.models import Reservation

from invoices.serializer import InvoiceSerializer
from invoices.models import Invoice


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        reservation_id = int(request.data['reservation_id'])
        reservation = Reservation.objects.get(pk=reservation_id)
        invoice = Invoice.objects.create(
            business_name=request.data['business_name'],
            nit=request.data['nit'],
            total=reservation.total,
            payment_method=request.data['payment_method'],
            reservation=reservation
        )
        reservation.state_reservation='Pagado'
        reservation.save()
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

@api_view(['GET'])
def invoice_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    invoice = Invoice.objects.filter(
        reservation=reservation
    )
    serializer = InvoiceSerializer(invoice, many=True)
    return Response(serializer.data)
