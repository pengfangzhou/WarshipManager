#encoding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from dbmodel.front.forms import CheckForm
from dbmodel.models import ZoneUrl
from dbmodel.front.dao import SoulDao
from dbmodel.front.dao import MatchDao
from dbmodel.front.dao import ProdRewordDao
from dbmodel.front import utils

def checkDrop(request):
    print "checkDrop()"
    # return HttpResponse("Hello world!")
    result = ""
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            result = 'not check'
            zone = form.cleaned_data['zone']
            checkTable = form.cleaned_data['checkTable']
            print "zone:",zone
            print "checkTable:",checkTable
            result = check(zone,checkTable)
            return render(request,'checkDrop.html',{'form':form,'result':result})
        print "form is not valid"
    else:
        print "query"
        form = CheckForm()
    return render(request,'checkDrop.html',{'form':form,'result':result})

def check(zone,table):
    result = ''
    if zone == 'all':
        zoneList = ZoneUrl.objects.all()
        for item in zoneList:
            name = item.name
            short = item.short
            ip = item.ip
            dbname = item.dbname
            print "short:",short
            print "ip:",ip
            print "zone:",zone
            result = result+"   ||__"+short+"_ "
            if table == 'match':
                result = result+checkMatch(name,short,ip,dbname)
            elif table == 'soulproba':
                result = result+checkSoul(name,short,ip,dbname)
            elif table == 'reward':
                result = result+checkReward(name,short,ip,dbname)

    else:
        items = ZoneUrl.objects.filter(short=zone)
        # print "items:",items
        if items and len(items)>0:
            item = items[0]
            name = item.name
            ip = item.ip
            dbname = item.dbname
            print "name:",name
            print "ip:",ip
            print "dbname:",dbname
            result = result+zone+"_ "
            if table == 'match':
                result = result+checkMatch(name,zone,ip,dbname)
            elif table == 'soulproba':
                result = result+checkSoul(name,zone,ip,dbname)
            elif table == 'reward':
                result = result+checkReward(name,zone,ip,dbname)
        else:
            result = result + zone + "is not find"
    return result

def checkProp(all):
    if all == None or len(all) <= 0:
        return 'match None'

    result = ''
    isOK = True
    for res in all:
        item = res[0]
        # print "item:",item
        props = item.split(',')
        # print "len props:",str(len(props))
        arr = utils.isPropInProps(props)

        if arr and len(arr)>0:
            isOK = False
            for r in arr:
                # print 'r:',r
                result = result+r+";"
    if isOK: result = 'props is ok'
    return result

def checkMatch(name,short,ip,dbname):
    print "checkMatch()"
    all = MatchDao.getAll(ip,dbname)
    result = checkProp(all)
    return result

def checkSoul(name,short,ip,dbname):
    print "checkSoul()"
    all = SoulDao.getAll(ip,dbname)
    result = checkProp(all)
    return result

def checkReward(name,short,ip,dbname):
    print "checkReward()"
    all = ProdRewordDao.getAll(ip,dbname)
    result = checkProp(all)
    return result









