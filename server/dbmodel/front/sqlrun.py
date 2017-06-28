#encoding=utf-8
from dbmodel.front.forms import SqlForm
from django.shortcuts import render
from dbmodel.models import ZoneUrl
from dbmodel.front.dao import sqlDao


def sqlQuery(request):
    print "sqlQuery()"
    error = ""
    if request.method == 'POST':
        form = SqlForm(request.POST)
        if form.is_valid():
            zone = form.cleaned_data['zone']
            sql = form.cleaned_data['sqls']
            code = form.cleaned_data['code']
            sqlmethod = form.cleaned_data['sqlmethod']
            sql = sql.strip()

            pp = u''
            #处理换行问题
            for tt in sql.splitlines():
                tt=tt.rstrip()+'\n'
                pp=pp+tt

            sql = pp

            # sql = sql.decode('utf-8')
            # sql = sql.encode('utf-8')

            # formatter = "%r"

            print "zone:",zone
            # print formatter % (sql)
            print "sql:",sql
            print "code:",code
            print "sqlmethod:",sqlmethod
            if code != 'sql89email765':
                error = u'号码出错'
                return render(request,'sqls.html',{'form':form,'error':error})
            if sqlmethod == 'query':
                resultarr = query(zone,sql)
            elif sqlmethod == 'execute':
                resultarr = execute(zone,sql)

            return render(request,'sqls.html',{'form':form,'resultarr':resultarr,'error':error})
        print "form is not valid"

    form = SqlForm()
    print "blank"
    return render(request,'sqls.html',{'form':form,'error':error})

def execute(zone,sql):
    print "execute()"
    sqlArr = sql.split(';')

    resultarr = []
    if zone == 'all':
        zoneList = ZoneUrl.objects.all()
        for item in zoneList:
            short = item.short
            name = item.name
            ip = item.ip
            gip = item.gip
            dbname = item.dbname

            for sqlItem in sqlArr:
                if sqlItem == None or sqlItem.strip() == '': continue
                results = sqlDao.executeSql(gip,dbname,sqlItem)
                item = {"name":name,"results":results}
                resultarr.append(item)
    else:
        items = ZoneUrl.objects.filter(short=zone)
        if items and len(items)>0:
            item = items[0]
            name = item.name
            ip = item.ip
            gip = item.gip
            dbname = item.dbname

            for sqlItem in sqlArr:
                if sqlItem == None or sqlItem.strip() == '': continue
                results = sqlDao.executeSql(gip,dbname,sqlItem)
                item = {"name":name,"results":results}
                resultarr.append(item)

        else:
            print zone," is not find"
    # print "resultarr:",resultarr

    return resultarr


def query(zone,sql):
    resultarr = []
    if zone == 'all':
        zoneList = ZoneUrl.objects.all()
        for item in zoneList:
            short = item.short
            name = item.name
            ip = item.ip
            gip = item.gip
            dbname = item.dbname
            results = sqlDao.queryQql(gip,dbname,sql)
            item = {"name":name,"results":results}
            resultarr.append(item)
    else:
        items = ZoneUrl.objects.filter(short=zone)
        if items and len(items)>0:
            item = items[0]
            name = item.name
            ip = item.ip
            gip = item.gip
            dbname = item.dbname
            results = sqlDao.queryQql(gip,dbname,sql)
            item = {"name":name,"results":results}
            resultarr.append(item)
        else:
            print zone," is not find"
    # print "resultarr:",resultarr

    return resultarr










