from django.db.models import Q

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rooms.serializer import RoomSerializer
from rooms.models import Room
from reservations.models import Reservation
from reservations_detail.models import DetailReservation


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @action(detail=False, methods=['GET'], name='Get free rooms')
    def freerooms(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        detail_reservations = DetailReservation.objects.filter(
            reservation__state_reservation='Pendiente'
        )
        rooms = Room.objects.filter(
            state=True
        ).exclude(
            id__in=detail_reservations.values('room_id')
        )
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
