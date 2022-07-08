from django.db import models

from challengegerente.util_model import TimeStamp

from reservations.models import Reservation


class Invoice(TimeStamp):
    """
    Model register invoice
        The class with attributes
            + id (Integer): Primary Key
            + business name (String): business name
            + nit (String): nit
            + city (String): invoice city
            + total (Float): total price
            + date (DateTime): datetime invoice
            + reservation (Integer): return reservation id
    """
    business_name = models.CharField(max_length=100)
    nit = models.CharField(max_length=50)
    total = models.FloatField()
    payment_method = models.CharField(max_length=50, default='Efectivo')
    date = models.DateTimeField(auto_now_add=True)
    reservation = models.OneToOneField(Reservation, on_delete=models.PROTECT)

    def __unicode__(self):
        return '%s - %s - %s' % (
            self.business_name,
            self.nit,
            self.total
        )

    def __str__(self):
        return '%s - %s - %s' % (
            self.business_name,
            self.nit,
            self.total
        )

    def get_date_invoice(self):
        return '%s' % self.date.strftime('%Y/%m/%d %H:%M')

    class Meta:
        """
        Meta Options
        """
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering = ['date']
