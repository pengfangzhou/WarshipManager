#encoding=utf-8
from dbmodel.front.forms import UserInfoForm
from django.shortcuts import render
from dbmodel.models import ZoneUrl
from dbmodel.front.dao import UserDao
import time
import utils

def userinfo(request):
    print "userinfo()"

    error = ""
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            startYear = form.cleaned_data['startYear']
            startMonth = form.cleaned_data['startMonth']
            startDay = form.cleaned_data['startDay']
            endYear = form.cleaned_data['endYear']
            endMonth = form.cleaned_data['endMonth']
            endDay = form.cleaned_data['endDay']
            code = form.cleaned_data['code']
            zone = form.cleaned_data['zone']

            startDayFull = str(startYear)+"-"+str(startMonth)+"-"+str(startDay)+" 00:00:00"
            endDayFull = str(endYear)+"-"+str(endMonth)+"-"+str(endDay)+" 23:59:00"
            querytime = "开始时间: "+startDayFull+"  结束时间: "+endDayFull

            if code != 'putao868988':
                error = "查询码出错"
                return render(request,'payinfo.html',{'form':form,'error':error})
            else:
                # resultDic = queryPay(startYear,startMonth,startDay,endYear,endMonth,endDay,zone)

                startTimestamp = utils.toTime(startDayFull)
                endTimestamp = utils.toTime(endDayFull)
                list = []
                if zone == 'all':
                    zoneList = ZoneUrl.objects.all()
                    for item in zoneList:
                        name = item.name
                        ip = item.ip
                        gip = item.gip
                        dbname = item.dbname
                        # print "dbname: ",dbname
                        result = queryUserNum(name,gip,dbname,startTimestamp,endTimestamp)
                        list.append(result)
                else:
                    items = ZoneUrl.objects.filter(short=zone)
                    if items and len(items)>0:
                        item = items[0]
                        name = item.name
                        ip = item.ip
                        gip = item.gip
                        dbname = item.dbname
                        # print "dbname: ",dbname

                        result = queryUserNum(name,gip,dbname,startTimestamp,endTimestamp)
                        list.append(result)
                    else:
                        print zone," is not find"

                return render(request,'userinfo.html',{'form':form,'error':error,'querytime':querytime,'results':list})
    else:
        nowTime = time.localtime(time.time())
        # nowTime = time.localtime()
        print "nowTime:",nowTime
        year = time.strftime("%Y",nowTime)
        month = time.strftime("%m",nowTime)
        day = time.strftime("%d",nowTime)
        form = UserInfoForm(initial={
            "startYear":year,
            "startMonth":month,
            "startDay":day,
            "endYear":year,
            "endMonth":month,
            "endDay":day,
        })
    return render(request,'userinfo.html',{'form':form,'error':error})

def queryUserNum(name,gip,dbname,startTimestamp,endTimestamp):
    # print "startTimestamp: ",startTimestamp
    # print "endTimestamp: ",endTimestamp

    userNum = UserDao.getAccountNumByDateTimestamp(gip,dbname,startTimestamp,endTimestamp)
    return {"zonename":name,"totalnum":userNum}
