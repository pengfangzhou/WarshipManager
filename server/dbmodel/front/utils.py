#encoding=utf-8
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

from dbmodel import models

def isPropInProps(cprops):
    arr = []
    for cprop in cprops:
        d = models.Props.objects.filter(propid=cprop)
        if d == None or len(d) <= 0:
            msg = cprop+" is not find."
            # print msg
            arr.append(msg)
        else:
            pname = d[0].name
            if pname == u'待定战姬':
                msg = cprop+" is 待定战姬."
                # print msg
                arr.append(msg)
    return arr

#将日期date转为时间time "2015-11-13 00:00:00"->1447344000
def toTime(myDay):
    #将字符串的时间转换为时间戳
    # # # 将其转换为时间数组
    timeArray = time.strptime(myDay,"%Y-%m-%d %H:%M:%S")
    # # # 转换为时间戳:
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


