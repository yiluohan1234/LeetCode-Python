#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2021年4月28日
#    > description: 
#######################################################################
'''
[231. 2的幂](https://leetcode-cn.com/problems/power-of-two/)
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
'''
import unittest
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (n&(n-1)) == 0
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 16
        res = True
        self.assertEqual(res, Solution().isPowerOfTwo(s))

if __name__ == "__main__":
    unittest.main()
