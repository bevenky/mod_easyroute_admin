from django.contrib import admin

from models import *


class LCRAdmin(admin.ModelAdmin):
    list_display = ('carrier', 'digits', 'rate', 'lead_strip', 'trail_strip', 'quality', \
                    'reliability', 'date_start', 'date_end', 'enabled', 'suffix', 'prefix', \
                    'lcr_profile', 'cid'
                    )
    list_filter = ['carrier', 'enabled', 'lcr_profile']
    search_fields = ['carrier__name', 'lcr_profile']
    list_per_page = 50
admin.site.register(LCR, LCRAdmin)
