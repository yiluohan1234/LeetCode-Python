#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月30日
#    > description: 
#######################################################################
'''
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

 
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
'''
import unittest
import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #1, get all the elements from the list.
        #2, sort all the elements
        #3, convert list to linklist
        tmp = []
        for i in lists:
            while i:
                tmp.append(i.val)
                i =  i.next
        tmp.sort()
        
        root = ListNode(0)
        p = root
        for i in range(len(tmp)): 
            p.next = ListNode(tmp[i])
            p = p.next
        return root.next
class Solution1:
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        first_half, second_half = lists[:len(lists)//2], lists[len(lists)//2:]
        first_half_sorted, second_half_sorted = self.mergeKLists(first_half), self.mergeKLists(second_half)

        dummy = ListNode()
        p1, p2 = first_half_sorted, second_half_sorted
        p = dummy

        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1:
            p.next = p1
        elif p2:
            p.next = p2

        return dummy.next   
class Solution2:
    def mergeKLists(self, lists):
        min_heap = []
        for list in lists: #for each sublist
            root = list #root = sublist head
            while root:
                heapq.heappush(min_heap, root.val) #we push to the list the value from each node
                root = root.next 
        
        head = curr = ListNode(None)
        
        while min_heap:
            curr.next = ListNode(heapq.heappop(min_heap))
            curr = curr.next
            
        return head.next    
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()