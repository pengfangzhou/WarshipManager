# -*- coding: utf-8 -*-

from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, include, url
from dbmodel.front.checkDrops import checkDrop
from dbmodel.front.payQuery import payinfo
from dbmodel.views import test
from dbmodel.views import update
from dbmodel.views import index
from dbmodel.views import info
from dbmodel.front.memberQuery import member
from dbmodel.front.sqlrun import sqlQuery
from dbmodel.front.UserInfoCount import userinfo
from dbmodel.views import testprods
from dbmodel.front.vipcompensation import doCompensation
from dbmodel import views

from dbmodel.front.handlers import mail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^server/', include('server.foo.urls')),

    # url(r'^accounts/login/$', auth_views.login),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # ('^checkdrop/$',checkDrop),
    ('^payinfo/$',payinfo),
    ('^test/$',test),
    ('^update/$',update),
    ('^$',index),
    ('^member/$',member),
    ('^sqlquery/$',sqlQuery),
    ('^info/$',info),

    ('^userinfo/$',userinfo),

    #GM 工具
    ('^login/$',views.login),
    ('^mail/$',mail.sendMail),


    # ('^prods/$',testprods),
    # ('^vipcompensation/$',doCompensation),
)
