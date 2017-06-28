# -*- coding: utf-8 -*-

from fabric.api import cd,run,env

env.warn_only = True

env.hosts = ['root@123.57.138.29',]
env.password = 'Asd868**123qwe'

# env.hosts = ['zhoupengfang@127.0.0.1',]
# env.password = ''

allZones = [0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16]
newZones = [12,13,14,15,16]


#执行新区
def donews():
    print "donews()"
    # newZones = [12]
    currZones = newZones

    # gitClone(currZones)

    # replaceNewConfig(currZones)
    # gitCommitAndPull(currZones)

    # createDjangoDB(currZones)

    jsonFile = "../../core_170207.json"
    loadJsonData(currZones,jsonFile)

#执行任务
def dotask():
    print "dotask()"
    currZones = allZones

    gitCommitAndPull(currZones)

#导入初始数据
def loadJsonData(zones,jsonFile):
    for zone in zones:
        rzone = zone+1
        print "rzone:",rzone
        rootdir = u'/root/srv/PtAcg/'
        prodir = rootdir+u'AcgServerS00'+str(rzone)+u'/src/'
        with cd(prodir):
            commandLoad = u"python manage.py loaddata "+jsonFile
            run(commandLoad)

#创建django数据库
def createDjangoDB(zones):
    for zone in zones:
        rzone = zone+1
        rootdir = u'/root/srv/PtAcg/'
        prodir = rootdir+u'AcgServerS00'+str(rzone)+u'/src/'
        with cd(prodir):
            run("python manage.py syncdb")

#替换新区数据
def replaceNewConfig(zones):
    print "replaceNewConfig()"
    for zone in zones:
        rzone = zone+1
        rootdir = u'/root/srv/PtAcg/'
        prodir = u'AcgServerS00'+str(rzone)+u'/src/'

        with cd(rootdir):
            #复制
            commandCP = "cp AcgServerS00"+str(rzone)+"/src/local_settings.py.sample AcgServerS00"+str(rzone)+"/src/local_settings.py"
            print "commandCP: ",commandCP
            run(commandCP)
            #替换
            commondSettingDBName = "sed -i 's/acg3/acg"+str(rzone)+"/g' "+prodir+"local_settings.py"
            print "commondSettingDBName: ",commondSettingDBName
            run(commondSettingDBName)

            commondSettingUrlName = "sed -i 's/s003/s00"+str(rzone)+"/g' "+prodir+"local_settings.py"
            run(commondSettingUrlName)

            commondSettingDBIDName = "sed -i 's/DATA_DBID = 3/DATA_DBID = "+str(rzone)+"/g' "+prodir+"local_settings.py"
            run(commondSettingDBIDName)

            commondSettingZONEIDName = "sed -i 's/ZONE_ID = 3/ZONE_ID = "+str(rzone)+"/g' "+prodir+"local_settings.py"
            run(commondSettingZONEIDName)

            newZonePort = '80'
            if rzone < 10:
                newZonePort = '8'+str(rzone)
            else:
                newZonePort = str(rzone)
            commondSettingPortName = "sed -i 's/8883/88"+str(newZonePort)+"/g' "+prodir+"local_settings.py"
            run(commondSettingPortName)

            #替换cron
            commandCron = "sed -i 's/127.0.0.1:8880/127.0.0.1:88"+str(newZonePort)+"/g' "+prodir+"script/cronrun.py"
            run(commandCron)

#git clone
def gitClone(zones):
    for zone in zones:
        ser = u'AcgServerS00'+str(zone+1)
        print "开始处理: ",ser
        with cd('/root/srv/PtAcg/'):
            commandClone = 'git clone ssh://git@d.putaogame.com:21022/AcgServer.git '+ser
            print commandClone
            run(commandClone)

#git commit并pull
def gitCommitAndPull(zones):
    # servers = ['/root/srv/PtAcg/AcgServerS001/','/root/srv/PtAcg/AcgServerS002/','/root/srv/PtAcg/AcgServerS003/','/root/srv/PtAcg/AcgServerS004/','/root/srv/PtAcg/AcgServerS005/','/root/srv/PtAcg/AcgServerS006/']
    print "gitfresh()"
    # with cd("/Users/zhoupengfang/Documents/spaces/acgSpace/AcgServer/"):

    for zone in zones:
        ser = u'/root/srv/PtAcg/AcgServerS00'+str(zone+1)
        print "开始处理: ",ser
        with cd(ser):
            run('git commit -am "c"')
            run('git pull')


#简单的本地操作
def lsfab():
    with cd('~'):
        run('ls')

#简单命令
def hello():
    # name,value
    print("Hello world")