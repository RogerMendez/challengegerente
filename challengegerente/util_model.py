from django.db import models


class TimeStamp(models.Model):
    """
    Abstract model register created an modified
    The class provides every table with following attributes
        + created (DateTime): store the date time the object was created
        + modified (DateTime): store the date time the object was modified
    """
    created = models.DateTimeField(
        'Created ad',
        auto_now_add=True,
        help_text="Date time registered in created at"
    )
    modified = models.DateTimeField(
        'Modified at',
        auto_now=True,
        help_text="Date time registeres in modified at"
    )

    class Meta:
        """Meta options"""
        abstract = True