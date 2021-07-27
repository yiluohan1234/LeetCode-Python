#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : getIntersectionNode.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/21 13:05:14
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################


'''
剑指 Offer 52. 两个链表的第一个公共节点(https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)
输入两个链表，找出它们的第一个公共节点。

'''
import unittest
# Definition for singly-linked list.
class Solution:
    def getIntersectionNode(self, headA, headB):
        x, y = headA, headB
        while x != y:
            x = x.next if x else headB
            y = y.next if y else headA
        return x
    def getIntersectionNode1(self, headA, headB):
        d = {}
        while headA:
            d[headA] = headA
            headA = headA.next
        while headB:
            if d.get(headB):
                return headB
            headB = headB.next
        return None
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()