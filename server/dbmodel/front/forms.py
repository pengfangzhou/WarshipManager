# coding=utf-8
from django import forms
from dbmodel.models import ZoneUrl

ZONE_CHOICES = [
]
zoneList = ZoneUrl.objects.all()
# print "zoneList:",zoneList
for item in zoneList:
    short = item.short
    name = item.name
    ip = item.ip
    gip = item.gip
    dbname = item.dbname
    ZONE_CHOICES.append((short,name))

ZONE_CHOICES.append(('all',u'所有分区'))
# ZONE_CHOICES.append(('s000',u'本地'))



CHECK_TABLES = (
    ('match',u'战役'),
    ('soulproba',u'抽奖'),
    ('reward',u'普通抽奖'),
)
SHOW_METHODS = (
    ('detail',u'详单'),
    ('detailchannel',u'详单+渠道+ip'),
)
SQL_METHODS = (
    ('query',u'查询'),
    ('execute',u'执行'),
)

class NormalForm(forms.Form):
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label=u'选择分区')

class CheckForm(forms.Form):
    # a = forms.IntegerField()
    # checkTable = forms.CharField(
    #     label="(战役:match;抽奖:soulproba)表单:",
    #     max_length=100
        # widget=forms.Textarea
    # )
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label=u'选择分区')
    checkTable = forms.ChoiceField(choices=CHECK_TABLES,label=u'选择表单')

class PayQueryForm(forms.Form):
    startYear = forms.IntegerField(label=u"开始年(*如2016)")
    startMonth = forms.IntegerField(label=u"开始月(*如6)")
    startDay = forms.IntegerField(label=u"开始日(*如27)")
    endYear = forms.IntegerField(label=u"结束年(*如2016)")
    endMonth = forms.IntegerField(label=u"结束月(*如6)")
    endDay = forms.IntegerField(label=u"结束日(*如30)")
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label=u'选择分区')
    # showmethod = forms.ChoiceField(choices=SHOW_METHODS,label='表现形式')
    code = forms.CharField(label=u"查询码",max_length=100)

class MemberForm(forms.Form):
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label=u'选择分区')
    userid = forms.IntegerField(label=u"用户id")

class UserInfoForm(forms.Form):
    startYear = forms.IntegerField(label=u"开始年(*如2016)")
    startMonth = forms.IntegerField(label=u"开始月(*如6)")
    startDay = forms.IntegerField(label=u"开始日(*如27)")
    endYear = forms.IntegerField(label=u"结束年(*如2016)")
    endMonth = forms.IntegerField(label=u"结束月(*如6)")
    endDay = forms.IntegerField(label=u"结束日(*如30)")
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label=u'选择分区')
    # showmethod = forms.ChoiceField(choices=SHOW_METHODS,label='表现形式')
    code = forms.CharField(label=u"查询码",max_length=100)

class SqlForm(forms.Form):
    sqls = forms.CharField(max_length=90000,widget=forms.Textarea,label=u'sqls')
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label=u'选择分区')
    code = forms.CharField(max_length=200,label=u'号码')
    sqlmethod = forms.ChoiceField(choices=SQL_METHODS,label=u'执行方式')








