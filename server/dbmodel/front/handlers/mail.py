# coding=utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
import json

import D
from dbmodel.models import ZoneUrl
from dbmodel.front import utils

from dbmodel.front.dao import UserDao
from dbmodel.front.dao import MailDao
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def sendMail(request):
    print "sendMail()"
    current_user_set = request.user
    print "current_user_set: ",current_user_set

    if request.GET.has_key('zone'):
        zoneid = request.GET['zone']
        print "zoneid: ",zoneid
        items = ZoneUrl.objects.filter(short=zoneid)
        if (items and len(items)>0) or zoneid=='all':
            usertype = request.GET['usertype']
            print u"分区存在 usertype: ",usertype

            name = request.GET['name']
            mail = {}
            mail['sender'] = u"秘书"
            mail['to'] = name
            if request.GET.has_key('title'):
                mail['title'] = request.GET['title']
            if request.GET.has_key('content'):
                mail['content'] = request.GET['content']
            if request.GET.has_key('type'):
                mail['type'] = request.GET['type']
            #{"gold":5000, "rock":100, "feat":100, "prods":{"04001":200}}
            awards = {}
            if request.GET.has_key('gold'):
                awards['gold'] = request.GET['gold']
            if request.GET.has_key('rock'):
                awards['rock'] = request.GET['rock']
            if request.GET.has_key('feat'):
                awards['feat'] = request.GET['feat']
            prods = {}
            if request.GET.has_key('prod1'):
                if request.GET['prod1'] in D.PRODS:
                    prods[request.GET['prod1']] = request.GET['prod1_num']
            if request.GET.has_key('prod2'):
                if request.GET['prod2'] in D.PRODS:
                    prods[request.GET['prod2']] = request.GET['prod2_num']
            if request.GET.has_key('prod3'):
                if request.GET['prod3'] in D.PRODS:
                    prods[request.GET['prod3']] = request.GET['prod3_num']
            if request.GET.has_key('prod4'):
                if request.GET['prod4'] in D.PRODS:
                    prods[request.GET['prod4']] = request.GET['prod4_num']
            if request.GET.has_key('prod5'):
                if request.GET['prod5'] in D.PRODS:
                    prods[request.GET['prod5']] = request.GET['prod5_num']
            awards['prods'] = prods
            mail['jawards'] = awards
            # red.lpush('mail:%s' % zoneid, pickle.dumps(mail))

            mail["msg"] = str(current_user_set)
            print "mail: ",mail

            results = None
            if usertype == 'single':
                #发送给单个用户
                results = sendMailToSingleUserSingleZone(items[0],mail['to'],mail)
            elif usertype == 'all':
                #发送给所有用户
                if zoneid == 'all':
                    #发送给所有分区
                    results = sendMailAllZonesAllUsers(mail)
                else:
                    #发送给单个分区所有用户
                    results = sendMailToSingleZoneAllUsers(items[0],mail)

            if results:
                print u"邮件发送成功. mail:",mail
                return HttpResponse(json.dumps(dict(error=u"邮件发送成功")), mimetype="application/json", status=200)
            else:
                print u"------邮件发送不成功. mail:",mail
                return HttpResponse(json.dumps(dict(error=u"邮件发送不成功")), mimetype="application/json", status=200)
        else:
            return HttpResponse(json.dumps(dict(error=u"分区不存在")), mimetype="application/json", status=404)

    zones = utils.getAllZonesChoice()

    # return render_to_response('mail.html')
    # return render_to_response('mail.html',{'zones':forms.ZONE_CHOICES})
    return render(request,'mail.html',{'zones':zones})



#发送给所有区所有用户
def sendMailAllZonesAllUsers(mail):
    # print u"发送给单分区所有用户"
    zoneList = ZoneUrl.objects.all()
    results = []
    for item in zoneList:
        result = sendMailToSingleZoneAllUsers(item,mail)
        results.append(result)
    return results

#发送给单分区所有用户
def sendMailToSingleZoneAllUsers(zoneItem,mail):
    print u"发送给单分区所有用户: ",zoneItem.name
    allUserIdsRes = UserDao.getAllUserids(zoneItem.gip,zoneItem.dbname)
    results = []
    for res in allUserIdsRes:
        to_userid, = res
        result = sendMailToSingleUserSingleZone(zoneItem,to_userid,mail)
        results.append(result)
    return results

#发送给单区单用户
def sendMailToSingleUserSingleZone(zoneItem,to_userid,mail):
    zoneName = zoneItem.name
    ip = zoneItem.ip
    gip = zoneItem.gip
    dbname = zoneItem.dbname
    # print "zone zoneName: ",zoneName

    mail['to'] = to_userid
    result = MailDao.sendMail(ip=gip,dbname=dbname,sender=mail["sender"],to_id=mail["to"], title=mail["title"], content=mail["content"], awards=mail["jawards"], msg=mail["msg"])
    return result



