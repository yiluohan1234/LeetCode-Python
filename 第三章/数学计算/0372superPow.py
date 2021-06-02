#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2021年4月28日
#    > description: 
#######################################################################
'''
[372. 超级次方](https://leetcode-cn.com/problems/super-pow/)
你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

 
'''
import unittest
class Solution(object):
    def __init__(self):
        self.base = 1337
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # a^[1,5,4] = a^4*(a^[1,5]) ^10
        if len(b) == 0:
            return 1
        last = b[-1]
        b.pop()

        part1 = self.myPow1(a, last)
        part2 = self.myPow1(self.superPow(a, b), 10)

        return (part1*part2) % self.base
    def myPow(self, a, k):
        # (a*b)%c = (a%c)(b%c)%c
        if k == 0:
            return 1
        ans = 1
        for i in range(k):
            ans *= a
            ans %= self.base
        
        return ans%self.base
    def myPow1(self, a, k):
        # (a*b)%c = (a%c)(b%c)%c
        if k == 0:
            return 1
        ans = 1
        if k % 2 == 1:
            return (a*self.myPow1(a, k-1)) % self.base
        else:
            sub = self.myPow1(a, k/2)
            return (sub*sub) % self.base

        
class TestSolution(unittest.TestCase):
    def test_0(self):
        a = 2
        b = [3]
        res = 8
        self.assertEqual(res, Solution().superPow(a, b))
    def test_1(self):
        a = 2
        b = [1,0]
        res = 1024
        self.assertEqual(res, Solution().superPow(a, b))
    def test_2(self):
        a = 1
        b = [4,3,3,8,5,2]
        res = 1
        self.assertEqual(res, Solution().superPow(a, b))
    def test_1(self):
        a = 2147483647
        b = [2,0,0]
        res = 1198
        self.assertEqual(res, Solution().superPow(a, b))

if __name__ == "__main__":
    unittest.main()
