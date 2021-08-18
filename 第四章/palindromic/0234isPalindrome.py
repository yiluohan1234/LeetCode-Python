#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################
'''
[234. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/)
请判断一个链表是否为回文链表。
'''
import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverse1(self, head):
        # 注意为空的判断
        if not head:
            return head
        if head.next == None:
            return head
        
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last
    def reverse(self, head):
        pre = None
        cur = head
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    def isPalindrome(self, head):
        fast = head
        slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        if fast != None:
            slow = slow.next
            
        left = head
        right = self.reverse(slow)
        while right != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    def palindrome(self, s, l, r):
        while l > 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
    # 二叉树的遍历方式
    # def traverse(TreeNode root):
    #     # 前序遍历代码
    #     self.traverse(root.left);
    #     # 中序遍历代码
    #     self.traverse(root.right);
    #     # 后序遍历代码
    
    # 链表有前序遍历和后序遍历
    # def traverse(ListNode head):
    #     # 前序遍历代码
    #     self.traverse(head.next);
    #     # 后序遍历代码
    def isPalindrome1(self, head):
        self.left = head
        def traverse(right):
            if not right:
                return True
            res = traverse(right.next)
            # 后序遍历代码
            res = res and (right.val == self.left.val)
            self.left = self.left.next
            return res
        
        return traverse(self.left)
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()