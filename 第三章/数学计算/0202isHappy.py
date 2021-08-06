#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0202isHappy.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/03 15:28:20
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
202. 快乐数(https://leetcode-cn.com/problems/happy-number/)
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。
 
'''
import unittest
import sys
INT_MAX = sys.maxsize
class Solution(object):
    def isHappy(self, n):
        all_set = set()
        while n not in all_set:
            all_set.add(n)
            tmp = sum((map(lambda x: int(x) ** 2, str(n))))
            if tmp == 1:
                return True
            n = tmp
        return False
    def isHappy1(self, n):
        all_set = set()
        while n not in all_set:
            all_set.add(n)
            tmp = 0
            while n:
                n,mod = divmod(n,10)
                tmp += mod ** 2
            if tmp == 1:
                return True
            n = tmp
        return False
class TestSolution(unittest.TestCase):
    def test_0(self):
        n = 19
        res = True
        self.assertEqual(res, Solution().isHappy(n))
    def test_1(self):
        n = 2
        res = False
        self.assertEqual(res, Solution().isHappy(n))

if __name__ == "__main__":
    unittest.main()
