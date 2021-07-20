#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0033search.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/14 14:20:33
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
33. 搜索旋转排序数组(https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
'''
import unittest
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        # [4,5,6,7,0,1,2]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[lo]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        res = 4
        self.assertEqual(res, Solution().search(nums, target))
    def test_1(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        res = -1
        self.assertEqual(res, Solution().search(nums, target))

if __name__ == '__main__':
    unittest.main()