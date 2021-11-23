#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月3日
#    > description: 
#######################################################################
import unittest
class Solution(object):
    def quicksort(self, nums, lo, hi):
        """
        :type nums: List[int]
        :rtype: int
        """
        if hi > lo:
            p = self.partition(nums, lo, hi)
            self.quicksort(nums, lo, p)
            self.quicksort(nums, p+1, hi)
    def partition(self, nums, lo, hi):
        if lo == hi:
            return lo 
        mid = nums[lo]
        while lo < hi:
            while lo < hi and nums[hi] > mid:
                hi -= 1
            nums[lo] = nums[hi]
            while lo < hi and nums[lo] < mid:
                lo += 1
            nums[hi] = nums[lo]
        
        nums[lo] = mid 
        return lo
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [7, 3, 2, 5, 1, 4, 6]
        res = [2, 3]
        self.assertEqual(res, Solution().findRepeatNumber(s))

if __name__ == '__main__':
    s = [7, 3, 2, 5, 1, 4, 6]
    Solution().quicksort(s, 0, len(s)-1)
    print(s)
