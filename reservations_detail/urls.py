from django.urls import path
from rest_framework import routers

from reservations_detail.viewsets import DetailReservationViewSet

from . import viewsets

router = routers.SimpleRouter()


router.register('detail-reservation', DetailReservationViewSet)

urlpatterns = router.urls + [
    path(
        'detail-reservation/rooms/<int:reservation_id>',
        viewsets.rooms,
        name="detail-reservation-rooms"
    ),

]
