#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: 崔羽飞
#    > Mail: XXX@qq.com
#    > Created Time: 2021年4月28日
#    > description: 
#######################################################################
'''
[172. 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes/)
给定一个整数 n，返回 n! 结果尾数中零的数量。
'''
import unittest
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        dividor = 5
        while dividor <= n:
            res += n/dividor
            dividor *= 5
        return res
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 3
        res = 0
        self.assertEqual(res, Solution().trailingZeroes(s))
    def test_1(self):
        s = 5
        res = 1
        self.assertEqual(res, Solution().trailingZeroes(s))

if __name__ == "__main__":
    unittest.main()
