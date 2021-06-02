#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@@qq.com
#    > Created Time: 2021年4月1日
#    > description: 
#######################################################################
'''
[78. 子集](https://leetcode-cn.com/problems/subsets/)
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
'''
import unittest
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        self.res = []
        self.backtrack(nums, 0, path)
        return self.res
    def backtrack(self, nums, start, path):
        self.res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i+1, path)
            path.pop()
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1,2,3]
        res = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        self.assertEqual(res, Solution().subsets(nums))

if __name__ == "__main__":
    unittest.main()
