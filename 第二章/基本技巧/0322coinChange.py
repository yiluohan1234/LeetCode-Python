#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年4月28日
#    > description: 
#######################################################################
'''
[322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。
dp(n)=          0, n=0
       -1, n <0
       min(dp(n-coin)+1 |coin in coins, n>0
'''
import unittest
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 暴力递归
        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('inf')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1:
                    continue
                res = min(res, 1+subproblem)
            return res if res != float('inf') else -1
        return dp(amount)
    def coinChange1(self, coins, amount):
        #带备忘录的暴力递归
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('inf')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1:
                    continue
                res = min(res, 1+subproblem)
            # 计入备忘录
            memo[n] = res if res != float('inf') else -1
            return memo[n]
        return dp(amount)
    def coinChange2(self, coins, amount):
        #dp 数组的迭代解法
        dp = [amount + 1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])
        
        return -1 if (dp[amount] == amount + 1) else dp[amount]
            
class TestSolution(unittest.TestCase):
    def test_0(self):
        coins = [1, 2, 5] 
        amount = 11
        res = 3
        self.assertEqual(res, Solution().coinChange1(coins, amount))

if __name__ == "__main__":
    unittest.main()
