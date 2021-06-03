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
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

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
                if nums[i] > nums[j]:
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
#         top = [0 for _ in range(len(nums))]
        top = {}
        piles = 0
        
        for i in range(len(nums)):
            poker = nums[i]
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid
            
            if left == piles:
                piles += 1
            print("left=%d, poker=%d, piles=%d"%(left, poker, piles))

            top[left] = poker
        print(top)
        return piles
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [10,9,2,5,3,7,101,18]
        res = 4
        self.assertEqual(res, Solution().lengthOfLIS1(nums))
    def test_1(self):
        nums = [0,1,0,3,2,3]
        res = 4
        self.assertEqual(res, Solution().lengthOfLIS(nums))
    def test_2(self):
        nums = [7,7,7,7,7,7,7]
        res = 1
        self.assertEqual(res, Solution().lengthOfLIS(nums))

if __name__ == "__main__":
    unittest.main()

