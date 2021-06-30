#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月28日
#    > description: 
#######################################################################
'''
[55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
'''
import unittest
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        n = len(nums)
        farthest = 0
        for i in range(n):
            farthest = max(farthest, i + nums[i])
            
            if farthest <= i:
                return False 

            if farthest >= n - 1:
                return True
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [2,3,1,1,4]
        res = True
        self.assertEqual(res, Solution().canJump(nums))
    def test_1(self):
        nums = [3,2,1,0,4]
        res = False
        self.assertEqual(res, Solution().canJump(nums))

if __name__ == '__main__':
    unittest.main()