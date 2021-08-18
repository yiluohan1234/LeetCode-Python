#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0021mergeTwoLists.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/18 16:22:26
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
[21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

''' 
import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 虚拟头结点
        dummy = ListNode(-1)
        p, p1, p2 = dummy, l1, l2 

        while p1 != None and p2 != None:
            # 比较 p1 和 p2 两个指针
            # 将值较小的的节点接到 p 指针
            if p1.val > p2.val:
                p.next = p2 
                p2 = p2.next 
            else:
                p.next = p1 
                p1 = p1.next 
            # p 指针不断前进
            p = p.next 

        if p1 != None:
            p.next = p1
        
        if p2 != None:
            p.next = p2

        return dummy.next
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()