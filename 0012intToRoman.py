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
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
import unittest
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        s, q, m, n = '', num, 1, 5
        while q:
            q, r = divmod(q, 10)
            if 0 < r < 4: s= r*d[m] + s
            elif r == 4: s = d[m] + d[n] + s
            elif r == 5: s = d[n] + s
            elif 5 < r < 9: s = d[n] + (r-5)*d[m] + s
            elif r == 9: s = d[m] + d[10*m] + s
            m, n = m*10, n*10
        return s
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))
    def test_none_1(self):
        s = 58
        res = "LVIII"
        self.assertEqual(res, Solution().intToRoman(s))
    def test_none_2(self):
        s = 9
        res = "IX"
        self.assertEqual(res, Solution().intToRoman(s))
    def test_none_3(self):
        s = 4
        res = "IV"
        self.assertEqual(res, Solution().intToRoman(s))
    def test_none_4(self):
        s = 3
        res = "III"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()