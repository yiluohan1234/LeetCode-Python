#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0092reverseBetween.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/10 10:58:13
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
[92. 反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii/)
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

'''
import unittest
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # 后驱节点
        self.nxt_head = None
        if left == 1:
            return self.reverseN(head, right)
        
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head, n):
        #  反转以 head 为起点的 n 个节点，返回新的头结点    
        if n == 1:
            # 记录第 n + 1 个节点
            self.nxt_head = head.next
            return head 
        # 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n-1)
        head.next.next = head 
        # 让反转之后的 head 节点和后面的节点连起来
        head.next = self.nxt_head

        return last
    def reverseAB(self, a, b):
        # 翻转[a,b)的链表
        pre, cur, nxt = None , a, a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre

    def reverse(self, head):
        # 翻转整个链表
        pre, cur, nxt = None , head, head
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        head = [1,2,3,4,5]
        k = 2
        res = [2,1,4,3,5]
        self.assertEqual(res, Solution().reverseKGroup(head, k))

if __name__ == '__main__':
    unittest.main()
    
