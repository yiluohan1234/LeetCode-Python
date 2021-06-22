#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年10月9日
#    > description: 
#######################################################################
'''
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
 

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''
import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rty
        """
        if not head or not head.next: 
            return head
        head.next.next, head.next, head = head, self.swapPairs(head.next.next), head.next
        return head
#         prev, cur = dummy, dummy.next = ListNode(0), head
#         while cur and cur.next:
#             cur.next.next, cur.next, prev.next = prev.next, cur.next.next, cur.next
#             prev, cur = cur, cur.next
#         return dummy.next
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev,nxt=head,head.next
        while nxt:
            prev.val,nxt.val=nxt.val,prev.val
            if nxt.next:
                prev=prev.next.next
                nxt=nxt.next.next
            else:
                break
        return head 
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head:                                           # first (head) node exists
            h = head.next                                  # second node
            if h:                                          # second node exists => a pair exists
                h.next, head.next = head, h.next           # swap node pair, first node with second => 'h' is new head
                h.next.next = self.swapPairs(h.next.next)  # recurse on next pair head
                return h              # returns the new head of a swapped node pair
        return head                   # returns when a node pair doesn't exist
class Solution3:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        fnext = head.next
        fnnext = fnext.next
        head.next = self.swapPairs(fnnext)
        fnext.next = head
        return fnext
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()