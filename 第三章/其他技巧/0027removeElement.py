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
[27. 移除元素](https://leetcode-cn.com/problems/remove-element/)
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
 
'''
import unittest
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #[1,2,3,4,5],3
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
        return slow
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "babad"
        res = "bab"
        self.assertEqual(res, Solution().removeElement(s))

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.longestPalindrome(nums))