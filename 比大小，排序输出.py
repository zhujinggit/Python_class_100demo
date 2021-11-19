# -*- coding: utf-8 -*-
#@Author:吐司面包
#@Date:2021-11-19

'''
输入三个整数X,Y,Z，请把这三个数由小到大输出
方法1：利用列表的排序属性
方法2：对比替换位置
'''


x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))

#方法1
def order_list(x,y,z):
    input_list=[x,y,z]
    input_list.sort()
    print("方法1利用列表排序：",input_list)

#方法2
def order_list_maopao(x,y,z):
    input_list=[x,y,z]
    for i in range(1,len(input_list)):
        for j in range(0,len(input_list)-i):
            if(input_list[j]>input_list[j+1]):
                input_list[j],input_list[j+1]=input_list[j+1],input_list[j]  
    print("方法2冒泡排序：{0},{1},{2}:".format(input_list[0],input_list[1],input_list[2]))


order_list(x,y,z)
order_list_maopao(x,y,z)

