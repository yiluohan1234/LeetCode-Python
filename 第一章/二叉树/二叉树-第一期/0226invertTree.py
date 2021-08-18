#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0226invertTree.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/13 15:59:47
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
[226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)
翻转一棵二叉树。
'''
import unittest
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()