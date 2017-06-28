# -*- coding: utf-8 -*-
import psycopg2
from dbmodel.front import Config

def getAll(ip,dbname,startTimeStamp,endTimeStamp,zoneshort,zonename):
    # print "Soul get"
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)

    putaogameCursor = conn.cursor()
    putaogameQuery = "select cr.id,cr.user_id,cr.pid,cp.price,cr.created_at,cr.trans_no from core_payrecord cr join core_product cp on cr.pid = cp.pid where cr.created_at>=%s and cr.created_at<=%s;"%(startTimeStamp,endTimeStamp,)
    putaogameAll = itemCursor(putaogameCursor,putaogameQuery)
    putaogameTotal = getTotalPrice(putaogameAll)

    xiaomiCursor = conn.cursor()
    xiaomiQuery = "select cr.id,cr.user_id,cr.pid,cp.price,cr.created_at,cr.app_order_id from core_xmpayrecord cr join core_product cp on cr.pid = cp.pid where cr.created_at>=%s and cr.created_at<=%s;"%(startTimeStamp,endTimeStamp,)
    xiaomiAll = itemCursor(xiaomiCursor,xiaomiQuery)
    xiaomiTotal = getTotalPrice(xiaomiAll)

    aliCursor = conn.cursor()
    aliQuery = "select cr.id,cr.user_id,cr.pid,cp.price,cr.created_at,cr.app_order_id from core_alipayrecord cr join core_product cp on cr.pid = cp.pid where cr.created_at>=%s and cr.created_at<=%s;"%(startTimeStamp,endTimeStamp,)
    aliAll = itemCursor(aliCursor,aliQuery)
    aliTotal = getTotalPrice(aliAll)

    letvCursor = conn.cursor()
    letvQuery = "select cr.id,cr.user_id,cr.pid,cp.price,cr.created_at,cr.app_order_id from core_letvpayrecord cr join core_product cp on cr.pid = cp.pid where cr.created_at>=%s and cr.created_at<=%s;"%(startTimeStamp,endTimeStamp,)
    letvAll = itemCursor(letvCursor,letvQuery)
    letvTotal = getTotalPrice(letvAll)

    chinamobileCursor = conn.cursor()
    chinamobileQuery = "select cr.id,cr.user_id,cr.pid,cp.price,cr.created_at,cr.app_order_id from core_cmpayrecord cr join core_product cp on cr.pid = cp.pid where cr.created_at>=%s and cr.created_at<=%s;"%(startTimeStamp,endTimeStamp,)
    chinamobileAll = itemCursor(chinamobileCursor,chinamobileQuery)
    chinamobileTotal = getTotalPrice(chinamobileAll)

    lovegameCursor = conn.cursor()
    lovegameQuery = "select cr.id,cr.user_id,cr.pid,cp.price,cr.created_at,cr.app_order_id from core_lgpayrecord cr join core_product cp on cr.pid = cp.pid where cr.created_at>=%s and cr.created_at<=%s;"%(startTimeStamp,endTimeStamp,)
    lovegameAll = itemCursor(lovegameCursor,lovegameQuery)
    lovegameTotal = getTotalPrice(lovegameAll)

    atetCursor = conn.cursor()
    atetQuery = "select cr.id,cr.user_id,cr.pid,cp.price,cr.paied_at,cr.app_order_id from core_atetpayrecord cr join core_product cp on cr.pid = cp.pid where cr.paied_at>=%s and cr.paied_at<=%s;"%(startTimeStamp,endTimeStamp,)
    atetAll = itemCursor(atetCursor,atetQuery)
    atetTotal = getTotalPrice(atetAll)

    shafaCursor = conn.cursor()
    shafaQuery = "select cr.id,cr.user_id,cr.pid,cp.price,cr.paytime,cr.app_order_id from core_pay_shafa_payrecord cr join core_product cp on cr.pid = cp.pid where cr.paytime>=%s and cr.paytime<=%s;"%(startTimeStamp,endTimeStamp,)
    shafaAll = itemCursor(shafaCursor,shafaQuery)
    shafaTotal = getTotalPrice(shafaAll)

    #当贝
    dangbeiCursor = conn.cursor()
    dangbeiQuery = "select cr.id,cr.user_id,cr.pid,cp.price,cr.paied_at,cr.app_order_id from core_dangbeipayrecord cr JOIN core_product cp on cr.pid=cp.pid where cr.paied_at>=%s and cr.paied_at<=%s;"%(startTimeStamp,endTimeStamp,)
    dangbeiAll = itemCursor(dangbeiCursor,dangbeiQuery)
    dangbeiTotal = getTotalPrice(dangbeiAll)

    conn.commit()
    conn.close()

    allTotal = putaogameTotal+xiaomiTotal+aliTotal+letvTotal+chinamobileTotal+lovegameTotal+atetTotal+shafaTotal+dangbeiTotal
    return {"zoneshort":zoneshort,"zonename":zonename,"putaogame":putaogameAll,"putaogameTotal":getTotalPrice(putaogameAll),"xiaomi":xiaomiAll,"xiaomiTotal":getTotalPrice(xiaomiAll),"ali":aliAll,"aliTotal":getTotalPrice(aliAll),"letv":letvAll,"letvTotal":getTotalPrice(letvAll),"chinamobile":chinamobileAll,"chinamobileTotal":getTotalPrice(chinamobileAll),"lovegame":lovegameAll,"lovegameTotal":getTotalPrice(lovegameAll),"atet":atetAll,"atetTotal":getTotalPrice(atetAll),"shafa":shafaAll,"shafaTotal":getTotalPrice(shafaAll),"dangbei":dangbeiAll,"dangbeiTotal":getTotalPrice(dangbeiAll),"allTotal":allTotal}

def itemCursor(cursor,query):
    cursor.execute(query)
    all = cursor.fetchall()
    return all


def getTotalPrice(all):
    total = 0
    if all:
        for item in all:
            total = total+item[3]
    return total
