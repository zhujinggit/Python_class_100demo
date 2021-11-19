# -*- coding: utf-8 -*-
#@Author:吐司面包
#@Date:2021-11-19

'''
输入某年某月某日，判断这一天是这一年的第几天？
特殊情况，闰年且输入月份大于3月时需要考虑多加一天。
'''

year = int(input("year:"))
month = int(input("month:"))
day = int(input("day"))

months=(0,31,59,90,120,151,181,212,243,273,304,334)

if(0<=month<=12):
    sum= months[month-1]+day
else:
    print("日期输入有误！")

if(year%400==0) or ((year%4==0) and (year%100==0)):
    if(month>2):
        sum+=1
print("日期{0}年{1}月{2}日，是当年的第{3}天".format(year,month,day,sum))
