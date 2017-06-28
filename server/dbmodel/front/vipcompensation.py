#encoding=utf-8
from dbmodel.front.forms import NormalForm
from django.shortcuts import render
from dbmodel.models import ZoneUrl
from dbmodel.front.dao import UserDao

def doCompensation(request):
    print "doCompensation()";
    result = ""
    if request.method == 'POST':
        form = NormalForm(request.POST)
        if form.is_valid():
            result = 'start '
            zone = form.cleaned_data['zone']
            print "zone:",zone
            # result = check(zone,checkTable)
            if zone == 'all':
                zoneList = ZoneUrl.objects.all()
                for item in zoneList:
                    ip = item.ip
                    gip = item.gip
                    dbname = item.dbname
                    print "dbname: ",dbname

                    result = result+" "+compensation(gip,dbname);
            else:
                items = ZoneUrl.objects.filter(short=zone)
                if items and len(items)>0:
                    item = items[0]
                    ip = item.ip
                    gip = item.gip
                    dbname = item.dbname
                    print "dbname: ",dbname

                    result = result+" "+compensation(gip,dbname);

                else:
                    print zone," is not find"


            return render(request,'normal.html',{'form':form,'result':result})
        print "form is not valid"
    else:
        print "query"
        form = NormalForm()

    return render(request,'normal.html',{'form':form,'result':result})

def compensation(gip,dbname):
    result = "    "+dbname+"开始补偿";

    list = UserDao.getAllUserByVRock(gip,dbname,1)
    if list == None:
        result = dbname+"没有vip用户"
        return result

    for item in list:
        userid = item["userid"]
        oldVrock = item["vrock"]
        newVrock = calNewVrockByOld(oldVrock)
        print "userid",str(userid)
        print "old vrock",str(oldVrock)
        print "newVrock",str(newVrock)

        uresult = UserDao.updateUserVRockByUserid(gip,dbname,userid,newVrock)
        if uresult:
            result = result+" "+str(userid)+" "+str(oldVrock)+" 改为: "+str(newVrock)+" 成功! |||    "
            print result
        else:
            result = str(userid)+" "+" 更新失败 "+str(oldVrock)+"  newVrock: "+str(newVrock)
            print result

    return result

def calNewVrockByOld(oldVrock):
    newVrock = 0
    if oldVrock>=150000:
        newVrock = oldVrock+350000
    elif oldVrock>=80000:
        newVrock = oldVrock+320000
    elif oldVrock>=40000:
        newVrock = oldVrock+260000
    elif oldVrock>=20000:
        newVrock = oldVrock+180000
    elif oldVrock>=15000:
        newVrock = oldVrock+145000
    elif oldVrock>=10000:
        newVrock = oldVrock+110000
    elif oldVrock>=7000:
        newVrock = oldVrock+73000
    elif oldVrock>=5000:
        newVrock = oldVrock+35000
    elif oldVrock>=3000:
        newVrock = oldVrock+17000
    elif oldVrock>=2000:
        newVrock = oldVrock+8000
    elif oldVrock>=1000:
        newVrock = oldVrock+4000
    elif oldVrock>=500:
        newVrock = oldVrock+1500
    elif oldVrock>=300:
        newVrock = oldVrock+600
    elif oldVrock>=100:
        newVrock = oldVrock+200
    elif oldVrock>=1:
        newVrock = oldVrock+9
    elif oldVrock>=0:
        newVrock = oldVrock
    return newVrock

