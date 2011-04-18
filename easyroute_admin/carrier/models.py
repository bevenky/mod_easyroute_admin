from django.db import models


class Carrier(models.Model):
    '''
    Carrier Class
    '''
    carrier_name = models.CharField(max_length=255, blank=False, null=False)
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % (self.carrier_name)

    class Meta:
        db_table = 'carriers'
        verbose_name = "Carrier"
        verbose_name_plural = "Carriers"


class CarrierGateway(models.Model):
    '''
    Carrier Gateway Class
    '''
    carrier = models.ForeignKey(Carrier)
    prefix = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    codec = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'carrier_gateway'
        verbose_name = "Carrier Gateway"
        verbose_name_plural = "Carrier Gateways"
