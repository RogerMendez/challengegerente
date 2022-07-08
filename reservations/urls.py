from django.urls import path
from rest_framework import routers

from reservations.viewsets import ReservationViewSet

router = routers.SimpleRouter()


router.register('reservation', ReservationViewSet)

urlpatterns = router.urls + [

]
