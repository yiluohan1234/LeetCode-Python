#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月29日
#    > description: 
#######################################################################
'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and 
return it as a new sorted list.
The new list should be made by splicing 
together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1 and l2 and l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next            
            elif l1 and l2 and l2.val <= l1.val:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()