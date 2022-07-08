from django.db import models

from challengegerente.util_model import TimeStamp

from rooms.models import Room
from reservations.models import Reservation

class DetailReservation(TimeStamp):
    """
    Model register detail reservation
        The class with attributes
            + id (Integer): Primary Key
            + customer name (String): customer name
            + customer phone (String): customer phone
            + customer address (String): customer address
            + customer genre (String): customer genre
            + reservation (Integer): return reservation id
            + room (Integer): return room id
    """
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10)
    customer_address = models.CharField(max_length=100)
    customer_genre = models.CharField(max_length=50)
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)

    def __unicode__(self):
        return '%s, %s' % (
            self.room.number,
            self.customer_name,
        )

    def __str__(self):
        return '%s, %s' % (
            self.room.number,
            self.customer_name,
        )

    class Meta:
        """"
        Meta Options
        """
        verbose_name = 'Detalle Reserva'
        verbose_name_plural = 'Detalle Reservaciones'
        ordering = ['reservation', 'room', 'customer_name']
