#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0081search.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/14 14:26:20
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
81. 搜索旋转排序数组 II(https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
'''
import unittest
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [2,5,6,0,0,1,2]
        target = 0
        res = True
        self.assertEqual(res, Solution().search(nums, target))
    def test_1(self):
        nums = [2,5,6,0,0,1,2]
        target = 3
        res = False
        self.assertEqual(res, Solution().search(nums, target))

if __name__ == '__main__':
    unittest.main()