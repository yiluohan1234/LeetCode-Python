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

不能用滑动窗口，数组中的数字有负数。
dp[i]:nums[0..i]中的「最大的子数组和」为dp[i],dp[i-1] 不能推出 dp[i]。
    因为子数组一定是连续的，按照我们当前dp数组定义，并不能保证nums[0..i]中的最大子数组与nums[i+1]是相邻的，也就没办法从dp[i]推导出dp[i+1]。
dp[i]:以nums[i]为结尾的「最大子数组和」为dp[i]。
    dp[i]有两种「选择」:
    要么与前面的相邻子数组连接，形成一个和更大的子数组；
    要么不与前面的子数组连接，自成一派，自己作为一个子数组。
    dp[i] = max(nums[i], nums[i] + dp[i - 1])
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
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        res = dp[0]
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

