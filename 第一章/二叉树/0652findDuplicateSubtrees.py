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
652. 寻找重复的子树
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
因此，你需要以列表的形式返回上述重复子树的根结点。
'''
import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.hmap = {}
        self.res = []
        self.postorder(root)
        return self.res
    def postorder(self, root):
        if not root:
            return "#"
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        subtree = left + ',' + right + ',' + str(root.val)
        count = self.hmap.get(subtree, 0)
        #多次重复也只会被加入结果集一次
        if count == 1:
            self.res.append(root)
        #给子树对应的出现次数加一
        self.hmap[subtree] = count + 1
        
        return subtree
                  

if __name__ == "__main__":
    unittest.main()