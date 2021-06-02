#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月19日
#    > description: 
#######################################################################
'''
[448. 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/)
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
'''
import unittest
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 当前元素是 nums[i]，那么我们把第 idx=nums[i]−1位置的元素 乘以 -1，表示这个该位置出现过。
        # 当然如果 第 nums[i]−1 位置的元素已经是负数了，表示 nums[i]已经出现过了，就不用再把第 nums[i]−1位置的元素乘以 -1。
        # 最后，对数组中的每个位置遍历一遍，如果 i 位置的数字是正数，说明 i+1未出现过。
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res. append(i+1)
        
        return res
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [4,3,2,7,8,2,3,1]
        res = [5,6]
        self.assertEqual(res, Solution().findDisappearedNumbers(s))

if __name__ == "__main__":
    unittest.main()
