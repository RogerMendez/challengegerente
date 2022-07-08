from django.db import models
from challengegerente.util_model import TimeStamp

TYPES_ROOM = (
    ('Simple', 'Simple'),
    ('Doble', 'Doble'),
    ('Triple', 'Triple'),
    ('Matrimonial', 'Matrimonial'),
)


class Room(TimeStamp):
    """
    Model register room
        The class with attributes
            + id (Integer): Primary Key
            + number (String): room number
            + type (String): type room (Simple, Doble, Triple, Matrimonial)
            + features (text): features room
            + price (Float): price room
            + state (Boolean): state room return true or false
    """
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=20, choices=TYPES_ROOM)
    features = models.TextField(null=True, blank=True)
    price = models.FloatField()
    state = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s, %s' % (self.number, self.type)

    def __str__(self):
        return '%s, %s' % (self.number, self.type)

    class Meta:
        """
        Meta Options
        """
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'
        ordering = ['number', 'type']
