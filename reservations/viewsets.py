from django.db.models import Max

from rest_framework import viewsets
# from rest_framework.decorators import api_view
from rest_framework.response import Response

from reservations.serializer import ReservationSerializer
from reservations.models import Reservation


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
