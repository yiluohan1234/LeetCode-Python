#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月10日
#    > description: 
#######################################################################
'''
[509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。
f(n) - 1, n=1, 2
    \
    \- f(n-1) + f(n-2) , n >2
'''
import unittest
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        # 暴力递归解法（自顶而下）
        if n == 1 or n == 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)
    
    def fib1(self, n):
        # 带备忘录的暴力递归解法（自顶而下）
        if n < 0:
            return 0
        memo = [0 for _ in range(n+1)]
        return self.Helper(memo, n)
    def Helper(self, memo, n):
        if n == 1 or n == 2:
            return 1
        if memo[n] != 0:
            return memo[n]
        memo[n] = self.Helper(memo, n-1) + self.Helper(memo, n-2)
        
        return memo[n]
    def fib2(self, n):
        # dp 数组迭代解法（自底而上）
        dp = [0 for _ in range(n+1)]
        dp[1] = dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 4
        res = 3
        self.assertEqual(res, Solution().fib2(s))

if __name__ == "__main__":
    unittest.main()
