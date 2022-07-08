from rest_framework import serializers

# Model Room
from rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ['created', 'modified']
