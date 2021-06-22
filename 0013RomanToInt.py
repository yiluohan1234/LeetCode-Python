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
13. Roman to Integer
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
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
import unittest
class Solution1(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        res += d[s[-1]]
        return res
class Solution2:
    def romanToInt(self, s):
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000         
        }
    
        sum = 0
        last_el = float('inf')
        for el in s:
            if last_el < d[el]:
                sum -= 2*last_el
                
            sum += d[el]
            last_el = d[el]               

        return sum       
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        res = 1994
        s = "MCMXCIV"
        self.assertEqual(res, Solution1().romanToInt(s))
    def test_none_1(self):
        res = 58
        s = "LVIII"
        self.assertEqual(res, Solution1().romanToInt(s))
    def test_none_2(self):
        res = 9
        s = "IX"
        self.assertEqual(res, Solution1().romanToInt(s))
    def test_none_3(self):
        res = 4
        s = "IV"
        self.assertEqual(res, Solution1().romanToInt(s))
    def test_none_4(self):
        res = 3
        s = "III"
        self.assertEqual(res, Solution1().romanToInt(s))
    def test_1_0(self):
        res = 1994
        s = "MCMXCIV"
        self.assertEqual(res, Solution2().romanToInt(s))
    def test_1_1(self):
        res = 58
        s = "LVIII"
        self.assertEqual(res, Solution2().romanToInt(s))
    def test_1_2(self):
        res = 9
        s = "IX"
        self.assertEqual(res, Solution2().romanToInt(s))
    def test_1_3(self):
        res = 4
        s = "IV"
        self.assertEqual(res, Solution2().romanToInt(s))
    def test_1_4(self):
        res = 3
        s = "III"
        self.assertEqual(res, Solution2().romanToInt(s))

if __name__ == "__main__":
    #unittest.main()
    s = ["flower","flow","flight"]
    print zip(*s)