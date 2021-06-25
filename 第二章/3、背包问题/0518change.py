#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月27日
#    > description: 
#######################################################################
'''
[518. 零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/)
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
'''
import unittest
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        # base case
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][amount]
            
class TestSolution(unittest.TestCase):
    def test_0(self):
        amount = 5
        coins = [1, 2, 5]
        res = 4
        self.assertEqual(res, Solution().change(amount, coins))
    def test_1(self):
        amount = 10
        coins = [10]
        res = 1
        self.assertEqual(res, Solution().change(amount, coins))
    def test_2(self):
        amount = 3
        coins = [2]
        res = 0
        self.assertEqual(res, Solution().change(amount, coins))

if __name__ == '__main__':
    unittest.main()