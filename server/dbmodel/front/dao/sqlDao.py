# -*- coding: utf-8 -*-
import psycopg2
from dbmodel.front import Config

def queryQql(ip,dbname,sql):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = sql
    cursor.execute(query)
    all = cursor.fetchall()
    results = []
    for item in all:
        itemlen = len(item)
        print "itemlen:",itemlen
        dups = []
        for i in xrange(0,itemlen):
            dups.append(item[i])
        results.append(dups)

    conn.commit()
    conn.close()
    return results

def executeSql(ip,dbname,sql):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = sql
    results = []
    dups = []
    print "sql:",sql
    try:
        cursor.execute(query)
        dups.append('ok')
        print "ok"
    except Exception,e:
        print e
        dups.append(e)

    dups.append(sql)
    results.append(dups)

    conn.commit()
    conn.close()
    return results