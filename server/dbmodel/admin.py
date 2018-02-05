# -*- coding: utf-8 -*-

from django.contrib import admin
from dbmodel.models import ZoneUrl
from dbmodel.models import Props
from dbmodel.models import MailLog

class ZoneUrlAdmin(admin.ModelAdmin):
    list_display = ('name','short','ip')

class PropsAdmin(admin.ModelAdmin):
    list_display = ('propid','name')

class MailLogAdmin(admin.ModelAdmin):
    list_display = ('userid', 'zid', 'mail', 'created_at')
    search_fields = ('userid', 'zid', 'created_at')
    fields = ('userid', 'mail', 'created_at')
    list_filter = ('userid', 'zid', 'created_at')

# admin.site.register(Props,PropsAdmin)
# admin.site.register(ZoneUrl,ZoneUrlAdmin)
admin.site.register(MailLog,MailLogAdmin)