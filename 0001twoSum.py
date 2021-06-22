#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name:0001twoSum.py 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年4月30日
#######################################################################
import unittest
"""
1. [Two Sum](https://leetcode.com/problems/two-sum/)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
1. [两数之和](https://leetcode.com/problems/two-sum/)
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
解题思路 
这道题最优的做法时间复杂度是 O(n)。
顺序扫描数组，对每一个元素，在 num_map中找能组合给定值的另一半数字，如果找到了，直接返回 2个数字的下标即可。
如果找不到，就把这个数字存入 num_map中，等待扫到“另一半”数字的时候，再取出来返回结果。
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i in range(len(nums)):
            another_num = target -nums[i]
            if another_num in num_map:
                return [num_map[another_num], i]
            else:
                num_map[nums[i]] =i
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        nums = [2,7,11,15]
        target = 9
        res = [0,1]
        self.assertEqual(res, Solution().twoSum(nums, target))

    def test_none_1(self):
        nums = [3,2,4] 
        target = 6
        res = [1,2]
        self.assertEqual(res, Solution().twoSum(nums, target))
    def test_none_2(self):
        nums = [3,3]
        target = 6
        res = [0,1]
        self.assertEqual(res, Solution().twoSum(nums, target))

if __name__ == "__main__":
    unittest.main()