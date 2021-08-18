#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月3日
#    > description: 
#######################################################################
'''
[25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''
import unittest
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        # 区间 [a, b) 包含 k 个待反转元素
        a, b = head, head
        for i in range(k):
            # 不足 k 个，不需要反转，base case
            if b == None:
                return head
            b = b.next
        # 反转前 k 个元素
        newHead = self.reverseAB(a, b)
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        
        return newHead
    
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
    
