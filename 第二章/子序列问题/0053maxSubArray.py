#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月24日
#    > description: 
#######################################################################
'''
[53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

'''
import unittest
import sys
max_value = sys.maxsize
min_value = -sys.maxsize - 1
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        # dp[i]:以nums[i]为结尾的最大子数组和 
        #状态：以前面子数组相连接，形成更大的子数组；不与前面子数组相连接，自成一派
        dp = [nums[0]]
        
        for i in range(1, len(nums)):
            dp.append(max(nums[i], nums[i] + dp[i-1]))
        res = min_value
        for i in range(len(dp)):
            res = max(res, dp[i])
        
        return res
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp_0 = nums[0]
        dp_1 = 0
        res = dp_0
        for i in range(1, len(nums)):
            dp_1 = max(nums[i], nums[i] + dp_0)
            dp_0 = dp_1
            res = max(res, dp_1)
        
        return res
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        res = 6
        self.assertEqual(res, Solution().maxSubArray(nums))
    def test_1(self):
        nums = [1]
        res = 1
        self.assertEqual(res, Solution().maxSubArray(nums))
    def test_2(self):
        nums = [0]
        res = 0
        self.assertEqual(res, Solution().maxSubArray(nums))
    def test_3(self):
        nums = [-1]
        res = -1
        self.assertEqual(res, Solution().maxSubArray(nums))
    def test_4(self):
        nums = [-100000]
        res = -100000
        self.assertEqual(res, Solution().maxSubArray(nums))

if __name__ == "__main__":
    unittest.main()

