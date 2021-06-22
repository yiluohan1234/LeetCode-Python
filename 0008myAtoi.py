#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月16日
#######################################################################
'''
8. String to Integer (atoi)
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''
import unittest
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        strNum = 0 
        positive = True
        if not str or len(str) == 0:
            return strNum
        if str[0] == '-' or str[0] == '+':
            if str[0] == '-':
                positive = False
            str = str[1:]
        for char in str:
            if char >= '0' and char <='9':
                strNum = strNum * 10 + ord(char) - ord('0')
            if char < '0' or char > '9':
                break
        if strNum > 2147483647:
            if not positive:
                return -2147483648
            else:
                return 2147483647
        if not positive:
            strNum = - strNum
        return strNum
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = "42"
        res = 42
        self.assertEqual(res, Solution().myAtoi(s))

    def test_none_1(self):
        s = "   -42"
        res = -42
        self.assertEqual(res, Solution().myAtoi(s))
    def test_none_2(self):
        s = "4193 with words"
        res = 4193
        self.assertEqual(res, Solution().myAtoi(s))
    def test_none_3(self):
        s = "words and 987"
        res = 0
        self.assertEqual(res, Solution().myAtoi(s))
    def test_none_4(self):
        s = "-91283472332"
        res = -2147483648
        self.assertEqual(res, Solution().myAtoi(s))

if __name__ == "__main__":
    unittest.main()