#encoding=utf-8

from django.db import models
import datetime

# Create your models here.
class ZoneUrl(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    short = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    dbname = models.CharField(max_length=50)
    gip = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Props(models.Model):
    id = models.AutoField(primary_key=True)
    propid = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.propid

class MailLog(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    zid = models.CharField(max_length=50)
    mail = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.userid







