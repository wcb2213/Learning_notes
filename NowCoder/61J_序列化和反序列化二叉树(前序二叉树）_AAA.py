w#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/4


# 26ms
# 序列化和反序列化二叉树
#  1. 对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
# 不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替。
#  2. 对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树(特别注意：
# 在递归时，递归函数的参数一定要是char ** ，这样才能保证每次递归后指向字符串的指针会
# 随着递归的进行而移动！！！)
#   BFS？
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root: return '#,'
        return str(root.val)+','+self.Serialize(root.left)+self.Serialize(root.right)
    def Deserialize(self, s):
        # write code here
        def recur():
            self.flag+=1
            ch=l[self.flag]
            if ch=='#': return None
            else:
                root=TreeNode(int(ch))
                root.left=recur()
                root.right=recur()
                return root
        self.flag=-1
        l=s.split(',')
        return recur()