#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0019removeNthFromEnd.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/19 10:18:14
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
[19. 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？

''' 
import unittest
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head 
        dummy = ListNode(-1)
        dummy.next = head 
        # 删除倒数第 n 个，要先找倒数第 n + 1 个节点
        x = self.findKthFromEnd(dummy, n+1)
        x.next = x.next.next 

        return dummy.next

    
    def findKthFromEnd(self, head, k):
        p1 = head 
        # p1 先走 k 步
        for i in range(k):
            p1 = p1.next 
        p2 = head 
        # p1 和 p2 同时走 n - k 步
        while p1 != None:
            p1 = p1.next 
            p2 = p2.next 
        # p2 现在指向第 n - k 个节点
        return p2
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = dummy
        while n and fast:
            fast = fast.next
            n -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()