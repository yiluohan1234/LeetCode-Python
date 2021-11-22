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
[300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

动态规划的核心设计思想是数学归纳法
dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。
base case。dp 数组应该全部初始化为 1，因为子序列最少也要包含自己，所以长度最小为 1
'''
import unittest
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        ans = 0
        for i in range(len(dp)):
            ans = max(ans, dp[i])
        
        return ans
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = {}
        # 初始化牌的顿数为0
        piles = 0
        
        for i in range(len(nums)):
            # 要处理的扑克牌
            poker = nums[i]
            # 左边界的二分查找
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                # if top[mid][-1] > poker:
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid
            # 没有找到合适的牌队，新建一堆
            if left == piles:
                piles += 1
            # 把这张牌放在堆顶
            top[left] = poker

        # 牌堆的个数就是LIS长度
        return piles
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [10,9,2,5,3,7,101,18]
        res = 4
        self.assertEqual(res, Solution().lengthOfLIS1(nums))
    def test_1(self):
        nums = [0,1,0,3,2,3]
        res = 4
        self.assertEqual(res, Solution().lengthOfLIS1(nums))
    def test_2(self):
        nums = [7,7,7,7,7,7,7]
        res = 1
        self.assertEqual(res, Solution().lengthOfLIS1(nums))

if __name__ == "__main__":
    unittest.main()

