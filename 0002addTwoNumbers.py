#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月9日
#######################################################################
import unittest
"""
2. [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
2. [两数相加](https://leetcode-cn.com/problems/add-two-numbers/)
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

"""
import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        carry = 0
        while l1 or l2 or carry != 0:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            # set value
            if sum <= 9:
                res.val = sum
                carry = 0
            else:
                res.val = sum%10
                carry = sum//10
            # creat new node
            if l1 or l2 or carry != 0:
                res.next = ListNode(0)
                res = res.next
        return head
class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """  
        if not l1 and not l2:
            return 
        elif not (l1 and l2):
            return l1 or l2
        else:
            if l1.val + l2.val < 10:
                l3 = ListNode(l1.val + l2.val)
                l3.next = self.addTwoNumbers(l1.next, l2.next) 
            else:
                l3 = ListNode(l1.val + l2.val - 10)
                l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, ListNode(1))) 
        return l3 
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        res = ListNode(7)
        res.next = ListNode(0)
        res.next.next = ListNode(8)
        self.assertEqual(res, Solution1().addTwoNumbers(l1, l1))

    def test_none_1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        res = ListNode(7)
        res.next = ListNode(0)
        res.next.next = ListNode(8)
        self.assertEqual(res, Solution2().addTwoNumbers(l1, l2))

# if __name__ == "__main__":
#     unittest.main()
if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    
    s1 = Solution1()
    s2 = Solution2()
    res = s2.addTwoNumbers(l1, l2)
    res_str = ""
    while res:
        res_str += str(res.val)
        res = res.next
    print(res_str)