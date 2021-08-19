#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0876middleNode.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/19 10:23:31
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
[876. 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list/)
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

''' 
import unittest
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 快慢指针初始化指向 head
        slow, fast = head, head 
        # 快指针走到末尾时停止
        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next 
        # 慢指针指向中点
        return slow
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()