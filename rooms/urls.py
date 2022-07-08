from django.urls import path
from rest_framework import routers

from rooms.viewsets import RoomViewSet

router = routers.SimpleRouter()


router.register('room', RoomViewSet)

urlpatterns = router.urls + [

]
