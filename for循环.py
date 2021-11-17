# -*- coding: utf-8 -*-
#@Author:吐司面包
#@Date:2021-11-15

'''
python经典100例：
第1例
for循环
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''

for d1 in range(1,5):
    for d2 in range(1,5):
        for d3 in range(1,5):
            if(d1!=d2) and (d2!=d3) and (d1!=d3):
                print(d1,d2,d3)
    