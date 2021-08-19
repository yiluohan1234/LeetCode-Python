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
[160. 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

'''
import unittest
# Definition for singly-linked list.
class Solution:
    def getIntersectionNode(self, headA, headB):
        # 我们可以让p1遍历完链表A之后开始遍历链表B，让p2遍历完链表B之后开始遍历链表A，这样相当于「逻辑上」两条链表接在了一起。
        # 如果这样进行拼接，就可以让p1和p2同时进入公共部分，也就是同时到达相交节点c1
        # a1->a2->c1->c2
        # b1->b2->b3->c1->c2
        # a1->a2->c1->c2->b1->b2->b3->c1
        # b1->b2->b3->c1->c2->a1->a2->c1
        p1, p2 = headA, headB
        while p1 != p2:
            # p1 走一步，如果走到 A 链表末尾，转到 B 链表
            p1 = p1.next if p1 else headB
            # p2 走一步，如果走到 B 链表末尾，转到 A 链表
            p2 = p2.next if p2 else headA
        return p1
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