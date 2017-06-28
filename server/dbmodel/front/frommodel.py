# -*- coding: utf-8 -*-

from django.forms import ModelForm
from dbmodel.models import ZoneUrl

class ZoneForm(ModelForm):
    class Meta:
        model = ZoneUrl
        fields = ('short','name')