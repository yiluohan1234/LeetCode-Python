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
337. 打家劫舍 III(https://leetcode-cn.com/problems/house-robber-iii/)
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1
输出: 7 
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1
输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
'''
import unittest
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def list_to_bitree(array):
    #判断arr是否为空
    if len(array) == 0:
        return TreeNode(array[0])
    mid=len(array) // 2 # 有序数组的中间元素的下标
    #print(mid)
    #start=0 # 数组第一个元素的下标
    #end=-1 # 数组最后一个元素的下标
    if len(array) > 0:
        #将中间元素作为二叉树的根
        root = TreeNode(array[mid])
        #如果左边的元素个数不为零，则递归调用函数，生成左子树
        if len(array[:mid]) > 0:
            root.left = list_to_bitree(array[:mid])
    #如果右边的元素个数不为零，则递归调用函数，生成左子树
    if len(array[mid+1:]) > 0:
        root.right = list_to_bitree(array[mid+1:])
    return root
class Solution(object):
    def __init__(self):
        self.memo = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        # 抢，然后去下下家
        do_it = root.val \
                + (0 if root.left == None else self.rob(root.left.left) + self.rob(root.left.right)) \
                + (0 if root.right == None else self.rob(root.right.left) + self.rob(root.right.right)) 
        # 不抢，然后去下家
        not_do = self.rob(root.left) + self.rob(root.right)
        res = max(do_it, not_do)
        self.memo[root] = res
        return res
    def rob1(self, root):
        res = self.dp(root)
        return max(res[0], res[1])
    def dp(self, root):
        # 返回一个大小为 2 的数组 arr
        # arr[0] 表示不抢 root 的话，得到的最大钱数
        # arr[1] 表示抢 root 的话，得到的最大钱数 
        if not root:
            return [0, 0]
        
        left = self.rob1(root.left)
        right = self.rob1(root.right)
        # 抢，下家就不能抢了
        rob = root.val + left[0] + right[0]
        # 不抢，下家可抢可不抢，取决于收益大小
        not_rob = max(left[0], left[1]) + max(right[0], right[1])
        
        return [not_rob, rob]
        
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [3,2,3,None,3,None,1]
        root = list_to_bitree(s)
        res = 7
        self.assertEqual(res, Solution().rob1(root))

if __name__ == '__main__':
    unittest.main()
    
