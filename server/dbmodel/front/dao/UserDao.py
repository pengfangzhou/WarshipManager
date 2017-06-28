# -*- coding: utf-8 -*-
import psycopg2
from dbmodel.front import Config

def getByUserid(ip,dbname,userid):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "select cu.id,ca.authstring,cu.nickname,cu.xp,cu.gold,cu.rock,cu.feat,cu.vrock from core_user cu JOIN core_account ca on cu.id=ca.user_id where cu.id=%s;"%userid
    cursor.execute(query)
    all = cursor.fetchall()

    conn.commit()
    conn.close()
    return all

def getByAllProds(ip,dbname):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "select cu.id,cu.jprods from core_user cu;"
    cursor.execute(query)
    all = cursor.fetchall()
    print "all:",all

    conn.commit()
    conn.close()
    return all

#获得有vip的用户
def getAllUserByVRock(ip,dbname,minVRock):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "select cu.id,cu.vrock from core_user cu where cu.vrock>=%s;"%minVRock
    cursor.execute(query)
    all = cursor.fetchall()
    print "all:",len(all)
    conn.commit()
    conn.close()

    if all == None or len(all) <= 0:
        return None

    list = []
    for res in all:
        userid = res[0]
        vrock = res[1]

        list.append({"userid":userid,"vrock":vrock})

    return list

#查询新增用户数
def getAccountNumByDateTimestamp(ip,dbname,startTimeStamp,endTimeStamp):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "select count(*) from core_account where created>=%s and created<=%s;"%(startTimeStamp,endTimeStamp)
    cursor.execute(query)
    all = cursor.fetchall()
    # print "all:",len(all)
    conn.commit()
    conn.close()

    if all == None or len(all) <= 0:
        return None
    return all[0][0]

#更新用户的vrock
def updateUserVRockByUserid(ip,dbname,userid,vrock):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "update core_user set vrock=%s where id=%s;"%(vrock,userid)
    try:
        cursor.execute(query)
    except Exception,e:
        print e
        return False

    conn.commit()
    conn.close()
    return True