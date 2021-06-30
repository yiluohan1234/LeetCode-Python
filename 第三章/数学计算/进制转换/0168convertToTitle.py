#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0168convertToTitle.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/06/30 12:17:26
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None   
#######################################################################
'''
[168. Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title/)
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
'''

import unittest
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ret = ''

        while columnNumber:
            # A-Z是1-26
            columnNumber -= 1
            columnNumber, num = divmod(columnNumber, 26)
            ret = chr(num + 65) + ret

        return ret
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        columnNumber = 2147483647
        res = "FXSHRXW"
        self.assertEqual(res, Solution().convertToTitle(columnNumber))
    def test_1(self):
        columnNumber = 701
        res = "ZY"
        self.assertEqual(res, Solution().convertToTitle(columnNumber))

if __name__ == '__main__':
    unittest.main()
    
