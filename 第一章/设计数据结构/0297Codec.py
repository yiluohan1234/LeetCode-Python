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
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]
 

Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''
import unittest
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: 
            return ""
        
        def dfs(node):
            if node is None:
                res.append('None')
                return ""
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        res = []
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        
        def dfs(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            root = TreeNode(l.pop(0))
            root.left = dfs(l)
            root.right = dfs(l)
            return root
        
        return dfs(data.split(','))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Codec().intToRoman(s))

if __name__ == "__main__":
    unittest.main()