from django.http import HttpResponse
from django.shortcuts import render
from dbmodel.models import ZoneUrl
from dbmodel.front.dao import sqlDao
from dbmodel.front.dao import UserDao
from dbmodel.front import ProdsUtils
import zlib
from cyclone import escape, web
import time

# Create your views here.
def test(request):
    print "test()"
    return HttpResponse("Hello world!")

def update(request):
    ret = dict(code=0, timestamp=int(time.time()))
    # reb = zlib.compress(escape.json_encode(ret))
    # self.write(ret)
    return HttpResponse("{\"code\": 0,\"timestamp\": 1492585823}")

def index(request):
    return render(request,'index.html',{})

def info(request):
    return render(request,'info.html',{})

def testprods(request):
    print "testprods()"
    zone = "s001"

    if zone == 'all':
        zoneList = ZoneUrl.objects.all()
        for item in zoneList:
            short = item.short
            name = item.name
            ip = item.ip
            gip = item.gip
            dbname = item.dbname

    else:
        items = ZoneUrl.objects.filter(short=zone)
        if items and len(items)>0:
            item = items[0]
            name = item.name
            ip = item.ip
            gip = item.gip
            dbname = item.dbname

            allProds = UserDao.getByAllProds(gip,dbname)
            print "allProds:",allProds
            prodArr = ProdsUtils.dealAllProds(allProds,'04002',10000)
            print ""
            print ""
            print ""
            print ""
            print ""
            print "prodArr:"
            print prodArr

        else:
            print zone," is not find"
    return HttpResponse("Run!")

