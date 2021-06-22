#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月16日
#    > description: 
#######################################################################
'''
[206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''
import unittest
class Solution(object):
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归方法
        if not head:
            return head

        if head.next == None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 迭代方法
        if not head:
            return head
        
        pre, cur, nxt = None, head, head
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre
    
class TestSolution(unittest.TestCase):
    def test_0(self):
        head = [1,2,3,4,5]
        res = [5,4,3,2,1]
        self.assertEqual(res, Solution().reverseList(head))

if __name__ == '__main__':
    unittest.main()
    
