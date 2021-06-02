#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2021年4月26日
#    > description: 
#######################################################################
'''
[560. 和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k/)
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

'''
import unittest
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[i] + nums[i])

        ans = 0
        for i in range(1,len(nums)+1):
            for j in range(i):
                if presum[i] - presum[j] == k:
                    ans += 1
        
        return ans
    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 前缀和->出现的次数，base
        presum = {0:1}

        ans, sumi = 0, 0
        for i in range(len(nums)):
            sumi += nums[i]
            sumj = sumi - k
            if sumj in presum:
                ans += presum[sumj]
            presum[sumi] = presum.get(sumi, 0) + 1
        
        return ans
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1,1,1] 
        k = 2
        res = 2
        self.assertEqual(res, Solution().subarraySum(nums, k))

if __name__ == "__main__":
    unittest.main()
