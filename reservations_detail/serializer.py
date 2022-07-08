from rest_framework import serializers

# Model Reservation Detal
from reservations_detail.models import DetailReservation


class DetailReservationSerializer(serializers.ModelSerializer):
    room_id = serializers.ReadOnlyField(source='room.id')
    room_number = serializers.ReadOnlyField(source='room.number')
    room_price = serializers.ReadOnlyField(source='room.price')
    room_type = serializers.ReadOnlyField(source='room.type')
    room_features = serializers.ReadOnlyField(source='room.features')

    class Meta:
        model = DetailReservation
        exclude = ['created', 'modified']
