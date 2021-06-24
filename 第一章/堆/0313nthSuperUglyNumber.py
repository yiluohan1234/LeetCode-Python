#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0313nthSuperUglyNumber.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/06/24 12:36:02
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
[313. 超级丑数](https://leetcode-cn.com/problems/super-ugly-number/)
编写一段程序来查找第 n 个超级丑数。
超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:
输入: n = 12, primes = [2,7,13,19]
输出: 32 
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
'''

import unittest
import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        hq = [1]
        ret = 1
        for i in range(n):
            tmp = heapq.heappop(hq)
            while hq and hq[0] == tmp:
                heapq.heappop(hq)
            for p in primes:
                heapq.heappush(hq, p * tmp)
            ret = tmp
        return ret
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 12
        res = 32
        self.assertEqual(res, Solution().nthSuperUglyNumber(s))

if __name__ == '__main__':
    unittest.main()
    
