# coding=utf-8
import datetime
import time
import os

PER_PERIOD = 60

def doSth5():
    print('doSth5: ',datetime.datetime.now())
    os.system("/usr/bin/python /Users/zhoupengfang/Documents/space/warshipSpace/WarshipServer/src/script/cronrun.py 5")

    # 假装做这件事情需要1小时
    time.sleep(60*PER_PERIOD)

def doSth9():
    print('doSth9: ',datetime.datetime.now())
    os.system("/usr/bin/python /Users/zhoupengfang/Documents/space/warshipSpace/WarshipServer/src/script/cronrun.py 9")

    # 假装做这件事情需要1小时
    time.sleep(60*PER_PERIOD)

def doSth12():
    print('doSth12: ',datetime.datetime.now())
    os.system("/usr/bin/python /Users/zhoupengfang/Documents/space/warshipSpace/WarshipServer/src/script/cronrun.py 12")

    # 假装做这件事情需要1小时
    time.sleep(60*PER_PERIOD)

def doSth18():
    print('doSth18: ',datetime.datetime.now())
    os.system("/usr/bin/python /Users/zhoupengfang/Documents/space/warshipSpace/WarshipServer/src/script/cronrun.py 18")

    # 假装做这件事情需要1小时
    time.sleep(60*PER_PERIOD)

def doSth21():
    print('doSth21: ',datetime.datetime.now())
    os.system("/usr/bin/python /Users/zhoupengfang/Documents/space/warshipSpace/WarshipServer/src/script/cronrun.py 21")

    # 假装做这件事情需要一分钟
    time.sleep(60*PER_PERIOD)

def cronMain():
    print "cronMain()"

    # 判断是否达到设定时间，例如0:00
    while True:
        now = datetime.datetime.now()
        print u"开始检测 now:",now
        # 到达设定时间，结束内循环
        if now.hour==5:
            doSth5()
        elif now.hour==9:
            doSth9()
        elif now.hour==12:
            doSth12()
        elif now.hour==18:
            doSth18()
        elif now.hour==21:
            doSth21()
        # 不到时间就等20分之后再次检测
        time.sleep(20*PER_PERIOD)


if __name__ == "__main__":
    print 'cronTimeMain '
    cronMain()
