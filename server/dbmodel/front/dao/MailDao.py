# coding=utf-8
import psycopg2
from dbmodel.front import Config
import datetime
from cyclone import web, escape

def sendMail(ip,dbname,sender, to_id, title, content, awards,msg=''):
    # print "sendMail()"

    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "INSERT INTO core_mail(sender, to_id, title, content, jawards, comment, created_at, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    params = (sender, to_id, title, content, escape.json_encode(awards), msg, datetime.datetime.now(), 0)

    cursor.execute(query,params)
    all = cursor.fetchall()
    conn.commit()
    conn.close()
    return all




