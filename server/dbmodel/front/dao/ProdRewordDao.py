# -*- coding: utf-8 -*-
import psycopg2
from dbmodel.front import Config

def getAll(ip,dbname):
    # print "Soul get"
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "select prod from core_prodreward;"
    cursor.execute(query)
    all = cursor.fetchall()
    conn.commit()
    conn.close()
    return all





