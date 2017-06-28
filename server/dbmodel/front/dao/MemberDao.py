# -*- coding: utf-8 -*-
import psycopg2
from dbmodel.front import Config

def getByAuth(ip,dbname,authstring):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "select cm.username,cm.channel,cm.realchannel,cm.source,cm.ip,cm.created from core_member cm where authstring='%s';"%authstring
    cursor.execute(query)
    all = cursor.fetchall()

    conn.commit()
    conn.close()
    return all