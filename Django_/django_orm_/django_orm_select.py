#!/usr/bin/python3
# file: django_orm_select.py
# Created by Guang at 19-9-30
# description: 内容参考了 运维开发吧

# *-* coding:utf8 *-*
User = None

################################ 基础操作 ###################################
# 获取所有数据，对应SQL：select * from User
User.objects.all()

# 匹配，对应SQL：select * from User where name = '运维咖啡吧'
User.objects.filter(name='运维咖啡吧')

# 不匹配，对应SQL：select * from User where name != '运维咖啡吧'
User.objects.exclude(name='运维咖啡吧')

# 获取单条数据（有且仅有一条，id唯一），对应SQL：select * from User where id = 724
User.objects.get(id=123)

################################ 常用操作 ###################################
# 获取总数，对应SQL：select count(1) from User
User.objects.count()

# 获取总数，对应SQL：select count(1) from User where name = '运维咖啡吧'
User.objects.filter(name='运维咖啡吧').count()

# 大于，>，对应SQL：select * from User where id > 724
User.objects.filter(id__gt=724)

# 大于等于，>=，对应SQL：select * from User where id >= 724
User.objects.filter(id__gte=724)

# 小于，<，对应SQL：select * from User where id < 724
User.objects.filter(id__lt=724)

# 小于等于，<=，对应SQL：select * from User where id <= 724
User.objects.filter(id__lte=724)

# 同时大于和小于， 1 < id < 10，对应SQL：select * from User where id > 1 and id < 10
User.objects.filter(id__gt=1, id__lt=10)

# 包含，in，对应SQL：select * from User where id in (11,22,33)
User.objects.filter(id__in=[11, 22, 33])

# 不包含，not in，对应SQL：select * from User where id not in (11,22,33)
User.objects.exclude(id__in=[11, 22, 33])

# 为空：isnull=True，对应SQL：select * from User where pub_date is null
User.objects.filter(pub_date__isnull=True)

# 不为空：isnull=False，对应SQL：select * from User where pub_date is not null
User.objects.filter(pub_date__isnull=True)

# 匹配，like，大小写敏感，对应SQL：select * from User where name like '%sre%'，SQL中大小写不敏感
User.objects.filter(name__contains="sre")

# 匹配，like，大小写不敏感，对应SQL：select * from User where name like '%sre%'，SQL中大小写不敏感
User.objects.filter(name__icontains="sre")

# 不匹配，大小写敏感，对应SQL：select * from User where name not like '%sre%'，SQL中大小写不敏感
User.objects.exclude(name__contains="sre")

# 不匹配，大小写不敏感，对应SQL：select * from User where name not like '%sre%'，SQL中大小写不敏感
User.objects.exclude(name__icontains="sre")

# 范围，between and，对应SQL：select * from User where id between 3 and 8
User.objects.filter(id__range=[3, 8])

# 以什么开头，大小写敏感，对应SQL：select * from User where name like 'sh%'，SQL中大小写不敏感
User.objects.filter(name__startswith='sre')

# 以什么开头，大小写不敏感，对应SQL：select * from User where name like 'sh%'，SQL中大小写不敏感
User.objects.filter(name__istartswith='sre')

# 以什么结尾，大小写敏感，对应SQL：select * from User where name like '%sre'，SQL中大小写不敏感
User.objects.filter(name__endswith='sre')

# 以什么结尾，大小写不敏感，对应SQL：select * from User where name like '%sre'，SQL中大小写不敏感
User.objects.filter(name__iendswith='sre')

# 排序，order by，正序，对应SQL：select * from User where name = '运维咖啡吧' order by id
User.objects.filter(name='运维咖啡吧').order_by('id')

# 多级排序，order by，先按name进行正序排列，如果name一致则再按照id倒叙排列
User.objects.filter(name='运维咖啡吧').order_by('name','-id')

# 排序，order by，倒序，对应SQL：select * from User where name = '运维咖啡吧' order by id desc
User.objects.filter(name='运维咖啡吧').order_by('-id')

################################ 进阶操作 ###################################
# limit，对应SQL：select * from User limit 3;
User.objects.all()[:3]

# limit，取第三条以后的数据，没有对应的SQL，类似的如：select * from User limit 3,10000000，从第3条开始取数据，取10000000条（10000000大于表中数据条数）
User.objects.all()[3:]

# offset，取出结果的第10-20条数据（不包含10，包含20）,也没有对应SQL，参考上边的SQL写法
User.objects.all()[10:20]

# 分组，group by，对应SQL：select username,count(1) from User group by username;
from django.db.models import Count
User.objects.values_list('username').annotate(Count('id'))

# 去重distinct，对应SQL：select distinct(username) from User
User.objects.values('username').distinct().count()

# filter多列、查询多列，对应SQL：select username,fullname from accounts_user
User.objects.values_list('username', 'fullname')

# filter单列、查询单列，正常values_list给出的结果是个列表，里边里边的每条数据对应一个元组，当只查询一列时，可以使用flat标签去掉元组，将每条数据的结果以字符串的形式存储在列表中，从而避免解析元组的麻烦
User.objects.values_list('username', flat=True)

# int字段取最大值、最小值、综合、平均数
from django.db.models import Sum,Count,Max,Min,Avg

User.objects.aggregate(Count(‘id’))
User.objects.aggregate(Sum(‘age’))

################################ 时间字段 ###################################
# 匹配日期，date
User.objects.filter(create_time__date=datetime.date(2018, 8, 1))
User.objects.filter(create_time__date__gt=datetime.date(2018, 8, 2))

# 匹配年，year
User.objects.filter(create_time__year=2018)
User.objects.filter(create_time__year__gte=2018)

# 匹配月，month
User.objects.filter(create_time__month__gt=7)
User.objects.filter(create_time__month__gte=7)

# 匹配日，day
User.objects.filter(create_time__day=8)
User.objects.filter(create_time__day__gte=8)

# 匹配周，week_day
 User.objects.filter(create_time__week_day=2)
User.objects.filter(create_time__week_day__gte=2)

# 匹配时，hour
User.objects.filter(create_time__hour=9)
User.objects.filter(create_time__hour__gte=9)

# 匹配分，minute
User.objects.filter(create_time__minute=15)
User.objects.filter(create_time__minute_gt=15)

# 匹配秒，second
User.objects.filter(create_time__second=15)
User.objects.filter(create_time__second__gte=15)


# 按天统计归档
today = datetime.date.today()
select = {'day': connection.ops.date_trunc_sql('day', 'create_time')}
deploy_date_count = Task.objects.filter(
    create_time__range=(today - datetime.timedelta(days=7), today)
).extra(select=select).values('day').annotate(number=Count('id'))

