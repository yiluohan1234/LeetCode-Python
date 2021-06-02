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
[645. 错误的集合](https://leetcode-cn.com/problems/set-mismatch/)
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。
请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

'''
import unittest
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup, err = -1, -1
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                dup = abs(nums[i])
            if nums[idx] > 0:
                nums[idx] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                err = i+1
        
        return [dup, err]

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [1,2,2,4]
        res = [2,3]
        self.assertEqual(res, Solution().findErrorNums(s))
    def test_1(self):
        s = [1,1]
        res = [1,2]
        self.assertEqual(res, Solution().findErrorNums(s))

if __name__ == "__main__":
    unittest.main()
