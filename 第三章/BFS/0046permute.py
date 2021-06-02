#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################
'''
[46. 全排列](https://leetcode-cn.com/problems/permutations/)
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]
'''
import unittest
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1,2,3]
        res = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        self.assertEqual(res, Solution().subsets(nums))

if __name__ == "__main__":
    unittest.main()
