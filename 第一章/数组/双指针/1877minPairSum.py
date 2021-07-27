#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 1877minPairSum.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/20 13:24:17
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
1877. 数组中最大数对和的最小值(https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array/)
一个数对 (a,b) 的 数对和 等于 a + b 。最大数对和 是一个数对数组中最大的 数对和 。

比方说，如果我们有数对 (1,5) ，(2,3) 和 (4,4)，最大数对和 为 max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8 。
给你一个长度为 偶数 n 的数组 nums ，请你将 nums 中的元素分成 n / 2 个数对，使得：

nums 中每个元素 恰好 在 一个 数对中，且最大数对和 的值 最小 。
请你在最优数对划分的方案下，返回最小的 最大数对和 。
'''

import unittest
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        lo, hi, ret = 0, len(nums) - 1, 0
        while lo < hi:
            ret = max(ret, nums[lo] + nums[hi])
            hi -= 1
            lo += 1

        return ret
    
    def minPairSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ln = len(nums)
        ret = 0

        for i in range(ln//2):
            ret = max(ret, nums[i] + nums[ln-i-1])
        
        return ret
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [3,5,2,3]
        res = 7
        self.assertEqual(res, Solution().minPairSum(nums))
    def test_1(self):
        nums = [3,5,4,2,4,6]
        res = 8
        self.assertEqual(res, Solution().minPairSum(nums))

if __name__ == '__main__':
    unittest.main()
    
