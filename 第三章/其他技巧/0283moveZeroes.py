#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月12日
#    > description: 
#######################################################################
'''
[283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
'''
import unittest
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = self.removeElement(nums, 0)
        for i in range(p, n):
            nums[i] = 0
        return nums
    def removeElement(self, nums, val):
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [0,1,0,3,12]
        res = [1,3,12,0,0]
        self.assertEqual(res, Solution().moveZeroes(s))

if __name__ == '__main__':
    unittest.main()