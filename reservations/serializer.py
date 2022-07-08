from rest_framework import serializers

# Model Reservation
from reservations.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        exclude = ['created', 'modified']
