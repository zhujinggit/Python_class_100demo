# -*- coding: utf-8 -*-
#@Author:吐司面包
#@Date:2021-11-19

import math
'''
一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
假设：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方
'''

for i in range(100000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if (x*x==i+100) and (y*y==i+268):
        print("该数是{0}".format(i))