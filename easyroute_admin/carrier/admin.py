from django.contrib import admin

from models import *


class CarrierAdmin(admin.ModelAdmin):
    list_display = ('carrier_name', 'enabled')
    list_filter = ['enabled']
    search_fields = ['carrier_name']
    list_per_page = 50
admin.site.register(Carrier, CarrierAdmin)


class CarrierGatewayAdmin(admin.ModelAdmin):
    list_display = ('carrier', 'prefix', 'suffix', 'codec', 'enabled')
    list_filter = ['codec', 'enabled']
    search_fields = ['carrier__name']
    list_per_page = 50
admin.site.register(CarrierGateway, CarrierGatewayAdmin)
