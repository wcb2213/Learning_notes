#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/2/24



# 26ms
# 调整list顺序时使用双指针降低损耗
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array)<=1: return array
        i,j=0,0
        while i<len(array):
            if array[i]%2==0:
                if j == len(array) - 1:
                    return array
                j=max(i+1,j+1)
                while array[j]%2==0:
                    if j==len(array)-1:
                        return array
                    j+=1
                tmp=array[j]
                for a in range(j,i,-1):
                    array[a]=array[a-1]
                array[i]=tmp
            i+=1
    # 调整数组序列 列表生成式
    # def reOrderArray(self, array):
    #     if len(array) == 0:
    #         return []
    #     l1 = [i for i in array if i%2 == 1]
    #     l2 = [i for i in array if i%2 == 0]
    #     return l1+l2