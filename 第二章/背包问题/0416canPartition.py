#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月26日
#    > description: 
#######################################################################
'''
[416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。


'''
import unittest
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        n = len(nums)
        if sum_nums % 2 == 1:
            return False
        sum_nums = int(sum_nums/2)
        dp =[[False for _ in range(sum_nums + 1)] for _ in range(n+1)]
        #base
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, sum_nums+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
        return dp[n][sum_nums]
    def canPartition1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        n = len(nums)
        if sum_nums % 2 == 1:
            return False
        sum_nums = int(sum_nums/2)
        dp =[False for _ in range(sum_nums + 1)]
        #base
        for i in range(n+1):
            dp[0] = True
        for i in range(1, n+1):
            for j in range(sum_nums, 0, -1):
                if j - nums[i-1] >= 0:
                    dp[j] = dp[j] or dp[j-nums[i-1]]
        
        return dp[sum_nums]
                    
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1,5,11,5]
        res = True
        self.assertEqual(res, Solution().canPartition1(nums))
    def test_1(self):
        nums = [1,2,3,5]
        res = False
        self.assertEqual(res, Solution().canPartition1(nums))

if __name__ == '__main__':
    unittest.main()