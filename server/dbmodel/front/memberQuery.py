#encoding=utf-8
from dbmodel.models import ZoneUrl
from dbmodel.front.forms import MemberForm
from django.shortcuts import render
from dbmodel.front.dao import UserDao
from dbmodel.front.dao import MemberDao
from dbmodel.front import Config

def member(request):
    # print "member"
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            zone = form.cleaned_data['zone']
            userid = form.cleaned_data['userid']
            items = ZoneUrl.objects.filter(short=zone)
            if items and len(items)>0:
                item = items[0]
                name = item.name
                ip = item.ip
                gip = item.gip
                dbname = item.dbname
                ress = UserDao.getByUserid(gip,dbname,userid)
                if ress and len(ress)>0:
                    userid,authstring,nickname,xp,gold,rock,feat,vrock = ress[0]
                    mress = MemberDao.getByAuth(Config.ZONE_GIP,Config.ZONE_DBNAME,authstring)
                    username,channel,realchannel,source,ip,created = mress[0]
                    return render(request,'member.html',{'form':form,'result':{"userid":userid,"authstring":authstring,"nickname":nickname,"xp":xp,"gold":gold,"rock":rock,"feat":feat,"vrock":vrock,"username":username,"channel":channel,"realchannel":realchannel,"source":source,"ip":ip,"created":created}})
                else:
                    return render(request,'member.html',{'form':form,'error':'未查到相关信息'})
    else:
        form = MemberForm()
    return render(request,'member.html',{'form':form})