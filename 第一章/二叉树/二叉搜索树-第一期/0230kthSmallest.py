#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################
from Cython.Debugger.Tests.TestLibCython import root
'''
230. Kth Smallest Element in a BST
Medium

3519

81

Add to List

Share
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

 

Example 1:
     3
   /   \
  1     4
   \   
    3 
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
         5
       /   \
      3     6
     / \    
    2   4  
   /
  1
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
'''
import unittest
class Solution(object):
    def inorder(self, root, A):
        if root.left:
            self.inorder(root.left, A)
        A.append(root.val)
        if root.right:
            self.inorder(root.right, A)
        
        return A
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return root
        A = []
        res = self.inorder(root, A)
        
        return res[k-1]
class Solution1(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val]  + inorder(root.right)
        
        return inorder(root)[k-1]

              
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()