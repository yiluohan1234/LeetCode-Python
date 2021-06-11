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
[98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''
import unittest
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, None, None)
    
    def isValid(self, root, minNode, maxNode):
        #限定以 root 为根的子树节点必须满足 max.val > root.val > min.val
        #base case
        if not root:
            return True
        #若 root.val 不符合 max 和 min 的限制，说明不是合法 BST
        if minNode != None and root.val <= minNode.val:
            return False
        if maxNode != None and root.val >= maxNode.val:
            return False
        #限定左子树的最大值是 root.val，右子树的最小值是 root.val
        return self.isValid(root.left, minNode, root) and self.isValid(root.right, root, maxNode)
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()