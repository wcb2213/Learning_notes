#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/28


# 27ms
# 构建乘积数组
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
class Solution:
    def multiply(self, A):
        # write code here
        n=len(A)
        B=[1]*n
        for i in range(1,n):
            B[i]=B[i-1]*A[i-1]
        tmp=1
        for i in range(n-2,-1,-1):
            tmp=tmp*A[i+1]
            B[i]=B[i]*tmp
        return B

if __name__ == '__main__':
    a = Solution()
    A = [1,2,3,4,5]
    print(a.multiply(A))