# -*- coding: utf-8 -*-

from django.contrib import admin
from dbmodel.models import ZoneUrl
from dbmodel.models import Props

class ZoneUrlAdmin(admin.ModelAdmin):
    list_display = ('name','short','ip')

class PropsAdmin(admin.ModelAdmin):
    list_display = ('propid','name')

admin.site.register(Props,PropsAdmin)
admin.site.register(ZoneUrl,ZoneUrlAdmin)
