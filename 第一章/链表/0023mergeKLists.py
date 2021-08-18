#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0023mergeKLists.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/18 16:20:20
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################


'''
[23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。  
''' 
import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        heap = []
        cur = dummy = ListNode(-1)
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        return dummy.next
        
    def mergeKLists(self, lists):
        import heapq
        dummy = ListNode(-1)
        p = dummy
        pq = []
        # 将 k 个链表的头结点加入最小堆
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(pq, (lists[i].val, lists[i]))
                
        while pq:
            # 获取最小节点，接到结果链表中
            val, node = heapq.heappop(pq)
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
            # p 指针不断前进
            p = p.next
        return dummy.next
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()