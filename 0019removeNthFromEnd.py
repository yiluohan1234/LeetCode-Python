#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月27日
#    > description: 
#######################################################################
'''
19. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''
import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p, q = dummy, dummy
        for i in range(n):
            q = q.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        
        return dummy.next
        
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(4)
        l1.next.next.next.next = ListNode(5)
        
        res = ListNode(1)
        res.next = ListNode(2)
        res.next.next = ListNode(3)
        res.next.next.next = ListNode(5)
        self.assertEqual(res, Solution().removeNthFromEnd(l1, 2))

if __name__ == "__main__":
    #unittest.main()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    res = Solution().removeNthFromEnd(l1, 2)
    i = 0
    res_print = []
    while res:
        res_print.append(res.val)
        res = res.next
    print(res_print)