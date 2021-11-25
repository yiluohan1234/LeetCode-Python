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
        if lo >= hi:
            return
        p = self.partition(nums, lo, hi)
        self.quicksort(nums, lo, p-1)
        self.quicksort(nums, p+1,hi)
        return nums
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
        res = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(res, Solution().quicksort(s, 0, len(s)-1))

if __name__ == '__main__':
    unittest.main()
    
