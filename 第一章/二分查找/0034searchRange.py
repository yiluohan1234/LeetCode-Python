#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0034searchRange.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/14 13:08:04
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
34. 在排序数组中查找元素的第一个和最后一个位置(https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
'''
import unittest
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = self.left_bound(nums, target)
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        hi = self.right_bound(nums, target)
        return [lo, hi]
    def left_bound(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        
        return lo 
    def right_bound(self, nums, target):
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                lo = mid + 1
        
        return lo - 1
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [5,7,7,8,8,10]
        target = 8
        res = [3, 4]
        self.assertEqual(res, Solution().searchRange(nums, target))
    def test_1(self):
        nums = [5,7,7,8,8,10]
        target = 6
        res = [-1, -1]
        self.assertEqual(res, Solution().searchRange(nums, target))

if __name__ == '__main__':
    unittest.main()
    