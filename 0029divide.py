#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################
'''
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
 

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
'''
import unittest
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if dividend^divisor >=0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        
        ans = 0 
        
        for power in range(31, -1, -1):
            if (divisor << power) <= dividend:
                ans += (1 << power)
                dividend -= (divisor << power)
        ans = ans*sign
        
        if not (-2**31 <= ans <= 2**31 - 1):
            return 2**31 - 1
        else:
            return ans
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        dividend = 10
        divisor = 3
        res = 3
        self.assertEqual(res, Solution().divide(dividend,divisor))
    def test_1(self):
        dividend = 7
        divisor = -3
        res = -2
        self.assertEqual(res, Solution().divide(dividend,divisor))
    def test_2(self):
        dividend = 0
        divisor = 1
        res = 0
        self.assertEqual(res, Solution().divide(dividend,divisor))
    def test_3(self):
        dividend = 1
        divisor = 1
        res = 1
        self.assertEqual(res, Solution().divide(dividend,divisor))
if __name__ == "__main__":
    unittest.main()