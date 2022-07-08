from rest_framework.decorators import api_view

from rest_framework import viewsets
from rest_framework.response import Response

from reservations_detail.serializer import DetailReservationSerializer
from reservations_detail.models import DetailReservation

from reservations.models import Reservation

from rooms.serializer import RoomSerializer
from rooms.models import Room


class DetailReservationViewSet(viewsets.ModelViewSet):
    queryset = DetailReservation.objects.all()
    serializer_class = DetailReservationSerializer

    def create(self, request, *args, **kwargs):
        reservation_id = int(request.data['reservation_id'])
        room_id = int(request.data['room_id'])
        new_detail = DetailReservation.objects.create(
            customer_address=request.data['customer_address'],
            customer_name=request.data['customer_name'],
            customer_genre=request.data['customer_genre'],
            customer_phone=request.data['customer_phone'],
            reservation_id=reservation_id,
            room_id=room_id,
        )
        reservation = new_detail.reservation
        days = (reservation.check_out - reservation.check_in).days
        reservation.total = reservation.total + (new_detail.room.price*days)
        reservation.save()
        serializer = DetailReservationSerializer(new_detail)
        return Response(serializer.data)


@api_view(['GET'])
def rooms(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    detail_reservations = DetailReservation.objects.filter(
        reservation=reservation
    )
    serializer = DetailReservationSerializer(detail_reservations, many=True)
    return Response(serializer.data)


