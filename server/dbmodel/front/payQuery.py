#encoding=utf-8
from dbmodel.front.forms import PayQueryForm
from django.shortcuts import render
import time
from dbmodel.models import ZoneUrl
from dbmodel.front.dao import PayDao

def payinfo(request):
    print "payinfo()"
    error = ""
    if request.method == 'POST':
        form = PayQueryForm(request.POST)
        if form.is_valid():
            startYear = form.cleaned_data['startYear']
            startMonth = form.cleaned_data['startMonth']
            startDay = form.cleaned_data['startDay']
            endYear = form.cleaned_data['endYear']
            endMonth = form.cleaned_data['endMonth']
            endDay = form.cleaned_data['endDay']
            # showmethod = form.cleaned_data['showmethod']
            code = form.cleaned_data['code']
            zone = form.cleaned_data['zone']
            if code != 'putao868988':
                error = "查询码出错"
                return render(request,'payinfo.html',{'form':form,'error':error})
            else:
                resultDic = queryPay(startYear,startMonth,startDay,endYear,endMonth,endDay,zone)
                return render(request,'payinfo.html',{'form':form,'error':error,'querytime':resultDic['querytime'],'results':resultDic['results']})
        print "form is not valid"
    else:
        print "query"
        nowTime = time.localtime(time.time())
        # nowTime = time.localtime()
        print "nowTime:",nowTime
        year = time.strftime("%Y",nowTime)
        month = time.strftime("%m",nowTime)
        day = time.strftime("%d",nowTime)
        form = PayQueryForm(initial={
            "startYear":year,
            "startMonth":month,
            "startDay":day,
            "endYear":year,
            "endMonth":month,
            "endDay":day,
        })
        # form['startYear'] = 2016
    return render(request,'payinfo.html',{'form':form,'error':error})

def queryPay(startYear,startMonth,startDay,endYear,endMonth,endDay,zone):
    querytime = "查询开始时间:%s 结束时间:%s"

    start = str(startYear)+"-"+str(startMonth)+"-"+str(startDay)+" 00:00:00"
    startTimeArray = time.strptime(start,"%Y-%m-%d %H:%M:%S")
    startTimeStamp = int(time.mktime(startTimeArray))

    end = str(endYear)+"-"+str(endMonth)+"-"+str(endDay)+" 23:59:59"
    endTimeArray = time.strptime(end,"%Y-%m-%d %H:%M:%S")
    endTimeStamp = int(time.mktime(endTimeArray))

    querytime = querytime%(start,end)

    results = []
    # results.append({"putaogameTotal":"300","xiaomiTotal":"100"})
    # results.append({"putaogameTotal":"200","xiaomiTotal":"200"})
    # results.append({"putaogameTotal":"100","xiaomiTotal":"500"})
    if zone == 'all':
        zoneList = ZoneUrl.objects.all()
        for item in zoneList:
            short = item.short
            name = item.name
            ip = item.ip
            gip = item.gip
            dbname = item.dbname
            # print "short:",short
            # print "ip:",ip
            # print "zone:",zone
            detail = queryDetailPay(startTimeStamp,endTimeStamp,short,name,ip,gip,dbname)
            results.append(detail)
    else:
        items = ZoneUrl.objects.filter(short=zone)
        if items and len(items)>0:
            item = items[0]

            name = item.name
            ip = item.ip
            gip = item.gip
            dbname = item.dbname
            # print "name:",name
            # print "ip:",ip
            # print "dbname:",dbname
            detail = queryDetailPay(startTimeStamp,endTimeStamp,zone,name,ip,gip,dbname)
            results.append(detail)
        else:
            print zone," is not find"

    print "results len:",str(len(results))
    return {"querytime":querytime,"results":results}

def queryDetailPay(startTimeStamp,endTimeStamp,short,zonename,ip,gip,dbname):
    # print "queryDetailPay()"
    detail = PayDao.getAll(gip,dbname,startTimeStamp,endTimeStamp,short,zonename)
    # print "detail:",detail
    return detail
























