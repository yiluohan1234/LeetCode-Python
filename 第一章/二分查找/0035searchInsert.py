#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0035searchInsert.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/14 12:57:31
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
35. 搜索插入位置(https://leetcode-cn.com/problems/search-insert-position/)
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
'''
import unittest
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid 
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        
        return lo 
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1,3,5,6]
        target = 5
        res = 2
        self.assertEqual(res, Solution().searchInsert(nums, target))
    def test_1(self):
        nums = [1,3,5,6]
        target = 2
        res = 1
        self.assertEqual(res, Solution().searchInsert(nums, target))

if __name__ == '__main__':
    unittest.main()
    
