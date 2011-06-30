from django.db import models

from carrier.models import Carrier


class LCR(models.Model):
    '''
    LCR Class
    '''
    carrier = models.ForeignKey(Carrier)
    digits = models.CharField(max_length=15, blank=True, null=True)
    rate = models.DecimalField(max_digits=11, decimal_places=5)
    lead_strip = models.PositiveIntegerField()
    trail_strip = models.PositiveIntegerField()
    quality = models.DecimalField(max_digits=10, decimal_places=6)
    reliability = models.DecimalField(max_digits=10, decimal_places=6)
    date_start = models.DateField()
    date_end = models.DateField()
    suffix = models.CharField(max_length=16, blank=True, null=True)
    prefix = models.CharField(max_length=16, blank=True, null=True)
    lcr_profile = models.CharField(max_length=32, blank=True, null=True)
    cid = models.CharField(max_length=32, blank=True, null=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'lcr'
        verbose_name = "Least Cost Route"
        verbose_name_plural = "Least Cost Routes"
