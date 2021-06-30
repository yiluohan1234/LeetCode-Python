#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0171titleToNumber.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/06/30 12:10:41
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
[171. Excel表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number/)
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

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
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ret = 0
        for i in columnTitle:
            # ret = ret * 26 + ord(i) - ord('A') + 1
            ret = ret * 26 + ord(i) - 64
        
        return ret
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        columnTitle = "A"
        res = 1
        self.assertEqual(res, Solution().titleToNumber(columnTitle))
    def test_1(self):
        columnTitle = "ZY"
        res = 701
        self.assertEqual(res, Solution().titleToNumber(columnTitle))

if __name__ == '__main__':
    unittest.main()
    
