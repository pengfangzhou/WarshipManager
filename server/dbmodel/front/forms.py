# coding=utf-8
from django import forms

ZONE_CHOICES = (
    ('all','所有分区'),
    ('s0017','帝国16区'),
    ('s0016','帝国15区'),
    ('s0015','帝国14区'),
    ('s0014','帝国13区'),
    ('s0013','帝国12区'),
    ('s0012','帝国11区'),
    ('s0011','帝国10区'),
    ('s0010','帝国9区'),
    ('s009','帝国8区'),
    ('s008','帝国7区'),
    ('s007','帝国六区'),
    ('s006','帝国五区'),
    ('s004','帝国三区'),
    ('s003','帝国二区'),
    ('s002','帝国一区'),
    ('s001','不删档区'),
    # ('s000','本地'),
)
ZONE_SINGLE = (
    ('all','所有分区'),
    ('s0017','帝国16区'),
    ('s0016','帝国15区'),
    ('s0015','帝国14区'),
    ('s0014','帝国13区'),
    ('s0013','帝国12区'),
    ('s0012','帝国11区'),
    ('s0011','帝国10区'),
    ('s0010','帝国9区'),
    ('s009','帝国8区'),
    ('s008','帝国7区'),
    ('s007','帝国六区'),
    ('s006','帝国五区'),
    ('s004','帝国三区'),
    ('s003','帝国二区'),
    ('s002','帝国一区'),
    ('s001','不删档区'),
    # ('s000','本地'),
)
CHECK_TABLES = (
    ('match','战役'),
    ('soulproba','抽奖'),
    ('reward','普通抽奖'),
)
SHOW_METHODS = (
    ('detail','详单'),
    ('detailchannel','详单+渠道+ip'),
)
SQL_METHODS = (
    ('query','查询'),
    ('execute','执行'),
)

class NormalForm(forms.Form):
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label='选择分区')

class CheckForm(forms.Form):
    # a = forms.IntegerField()
    # checkTable = forms.CharField(
    #     label="(战役:match;抽奖:soulproba)表单:",
    #     max_length=100
        # widget=forms.Textarea
    # )
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label='选择分区')
    checkTable = forms.ChoiceField(choices=CHECK_TABLES,label='选择表单')

class PayQueryForm(forms.Form):
    startYear = forms.IntegerField(label="开始年(*如2016)")
    startMonth = forms.IntegerField(label="开始月(*如6)")
    startDay = forms.IntegerField(label="开始日(*如27)")
    endYear = forms.IntegerField(label="结束年(*如2016)")
    endMonth = forms.IntegerField(label="结束月(*如6)")
    endDay = forms.IntegerField(label="结束日(*如30)")
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label='选择分区')
    # showmethod = forms.ChoiceField(choices=SHOW_METHODS,label='表现形式')
    code = forms.CharField(label="查询码",max_length=100)

class MemberForm(forms.Form):
    zone = forms.ChoiceField(choices=ZONE_SINGLE,label='选择分区')
    userid = forms.IntegerField(label="用户id")

class UserInfoForm(forms.Form):
    startYear = forms.IntegerField(label="开始年(*如2016)")
    startMonth = forms.IntegerField(label="开始月(*如6)")
    startDay = forms.IntegerField(label="开始日(*如27)")
    endYear = forms.IntegerField(label="结束年(*如2016)")
    endMonth = forms.IntegerField(label="结束月(*如6)")
    endDay = forms.IntegerField(label="结束日(*如30)")
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label='选择分区')
    # showmethod = forms.ChoiceField(choices=SHOW_METHODS,label='表现形式')
    code = forms.CharField(label="查询码",max_length=100)

class SqlForm(forms.Form):
    sqls = forms.CharField(max_length=90000,widget=forms.Textarea,label='sqls')
    zone = forms.ChoiceField(choices=ZONE_CHOICES,label='选择分区')
    code = forms.CharField(max_length=200,label='号码')
    sqlmethod = forms.ChoiceField(choices=SQL_METHODS,label='执行方式')








