from django.db import models

from challengegerente.util_model import TimeStamp
from rooms.models import Room


STATE_RESERVATION = (
    ('Pendiente', 'Pendiente'),
    ('Pagado', 'Pagado'),
    ('Eliminado', 'Eliminado'),
)

GENRE_TYPE = (
    ('Femenino', 'Femenino'),
    ('Masculino', 'Masculino'),
    ('No Corresponde', 'No Corresponde'),
)


class Reservation(TimeStamp):
    """
    Model register reservation
        The class with attributes
            + id (Integer): Primary Key
            + total (Float): total price
            + check in (DateTime): date of entry to the room
            + check out (DateTime): date of departure to the room
            + state reservation (String): reservation status
    """
    total = models.FloatField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    state_reservation = models.CharField(max_length=20, choices=STATE_RESERVATION)

    def __unicode__(self):
        return '%s, %s' % (self.check_in, self.check_out)

    def __str__(self):
        return '%s, %s' % (self.check_in, self.check_out)

    class Meta:
        """"
        Meta options
        """
        verbose_name = 'Reservación'
        verbose_name_plural = 'Reservaciones'
        ordering = ['check_in', 'check_out']
