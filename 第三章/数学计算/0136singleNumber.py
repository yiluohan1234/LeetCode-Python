#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: 崔羽飞
#    > Mail: XXX@qq.com
#    > Created Time: 2021年4月28日
#    > description: 
#######################################################################
import unittest
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res ^= n
        
        return res
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [2, 2, 1]
        res = 1
        self.assertEqual(res, Solution().singleNumber(s))

if __name__ == "__main__":
    unittest.main()
