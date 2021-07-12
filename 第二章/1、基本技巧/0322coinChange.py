#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月10日
#    > description: 
#######################################################################
'''
[322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。
dp(n) =  0, n=0
        -1, n <0
        min(dp(n-coin)+1 |coin in coins, n>0
如何列出状态转移方程？
1、明确状态。原问题和子问题中变化的变量。硬币数量无限，唯一的状态就是目标金额amount。
2、定义dp数组或函数的定义。dp(n)：当前目标金额为n，至少需要dp(n)个金币凑出目标金额。
3、明确「选择」并择优。从coins中选择一个硬币，目标金额减少
# 伪码框架
def coinChange(coins: List[int], amount: int):
    # 定义：要凑出金额 n，至少要 dp(n) 个硬币
    def dp(n):
        # 做选择，需要硬币最少的那个结果就是答案
        for coin in coins:
            res = min(res, 1 + dp(n - coin))
        return res
    # 我们要求目标金额是 amount
    return dp(amount)
4、明确 base case。目标金额为 0 时，所需硬币数量为 0；当目标金额小于 0 时，无解，返回 -1
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
                # subproblem = dp(n-coin)
                if n-coin < 0:
                    continue
                res = min(res, 1 + dp(n-coin))
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
           for j in range(0, len(coins)):
                if i - coins[j] < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        
        return -1 if (dp[amount] == amount + 1) else dp[amount]
            
class TestSolution(unittest.TestCase):
    def test_0(self):
        coins = [1, 2, 5] 
        amount = 11
        res = 3
        self.assertEqual(res, Solution().coinChange1(coins, amount))

if __name__ == "__main__":
    unittest.main()
