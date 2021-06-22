#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 0516longestPalindromeSubseq.py
#    > Time     : 2021/06/17 10:17:58
#    > Author   : Cui Yufei 
#    > Version  : 1.0
#    > Email    : 1097189275@qq.com
#    > License  : (C)Copyright 2017-2018, XXX
#    > Desc     : None
#######################################################################


import unittest
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
   
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [2, 3, 1, 0, 2, 5, 3]
        res = [2, 3]
        self.assertEqual(res, Solution().findRepeatNumber(s))

if __name__ == '__main__':
    unittest.main()

