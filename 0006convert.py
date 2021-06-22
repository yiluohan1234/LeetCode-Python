#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月15日
#######################################################################
import unittest
'''
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        idx, step = 0, 1
        res = ['']*numRows
        for x in s:
            res[idx] += x
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return ''.join(res)
            
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = "PAYPALISHIRING"
        numRows = 3
        res = "PAHNAPLSIIGYIR"
        self.assertEqual(res, Solution().convert(s, numRows))

    def test_none_1(self):
        s = "PAYPALISHIRING"
        numRows = 4
        res = "PINALSIGYAHRPI"
        self.assertEqual(res, Solution().convert(s, numRows))

if __name__ == "__main__":
    unittest.main()