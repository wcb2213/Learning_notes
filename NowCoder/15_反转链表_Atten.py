#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/26


# 24ms
# 反转链表后，输出新链表的表头
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        ph,re=pHead,None
        while ph:
            tmp=ph.next
            ph.next=re
            re=ph
            ph=tmp
        return re