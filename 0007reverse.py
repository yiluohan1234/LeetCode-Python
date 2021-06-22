#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月16日
#######################################################################
'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the 
reversed integer overflows.
'''
import unittest
import operator
class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mark = 1 if x >= 0 else  -1
        x_abs = abs(x)
        res = mark * int(str(x_abs)[::-1])
        return res if -2**31 <= x <= 2**31 -1 else 0
class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """  
        if x < 0:
            return -self.reverse(-x)
        res = 0
        while x:
            res = res * 10 + x%10
            x = x//10
        return res if x <= 0x7fffffff else 0
class Solution3(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """  
        res = -int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])
        res = 0 if abs(res) > 0x7FFFFFFF else res
        return res 
class Solution4(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        https://blog.csdn.net/joeyon1985/article/details/38901723
        """
#         s = cmp(x, 0)
#         r = int(`s * x`[::-1])
        s = 1 if operator.gt(x,0) else -1
        r = int(str(s*x)[::-1])
        return s * r * (r < 2 ** 31)   
   
class TestSolution(unittest.TestCase):
    def test_s1_0(self):
        nums = 123
        res = 321
        self.assertEqual(res, Solution1().reverse(nums))
    def test_s1_1(self):
        nums = -123 
        res = -321
        self.assertEqual(res, Solution1().reverse(nums))
    def test_s1_2(self):
        nums = 120
        res = 21
        self.assertEqual(res, Solution1().reverse(nums))
        
    def test_s2_0(self):
        nums = 123
        res = 321
        self.assertEqual(res, Solution2().reverse(nums))
    def test_s2_1(self):
        nums = -123 
        res = -321
        self.assertEqual(res, Solution2().reverse(nums))
    def test_s2_2(self):
        nums = 120
        res = 21
        self.assertEqual(res, Solution2().reverse(nums))
    
    def test_s3_0(self):
        nums = 123
        res = 321
        self.assertEqual(res, Solution3().reverse(nums))
    def test_s3_1(self):
        nums = -123 
        res = -321
        self.assertEqual(res, Solution3().reverse(nums))
    def test_s3_2(self):
        nums = 120
        res = 21
        self.assertEqual(res, Solution3().reverse(nums))
    
    def test_s4_0(self):
        nums = 123
        res = 321
        self.assertEqual(res, Solution4().reverse(nums))
    def test_s4_1(self):
        nums = -123 
        res = -321
        self.assertEqual(res, Solution4().reverse(nums))
    def test_s4_2(self):
        nums = 120
        res = 21
        self.assertEqual(res, Solution4().reverse(nums))

if __name__ == "__main__":
    unittest.main()