#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月1日
#    > description: 
#######################################################################
'''
[121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
给定一个数组 prices ，它的第 i个元素 prices[i] 表示一支给定股票第 i天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
'''
import unittest
'''
for 状态1 in 状态1的所有值:
    for 状态2 in 状态2的所有值:
        for ... 
            dp[状态1][状态2][...] = 择优(选择1, 选择2, ...)

dp[i][k][0]:「状态」有三个，第一个是天数，第二个是当天允许交易的最大次数，第三个是当前的持有状态（即之前说的 rest 的状态，我们不妨用 1 表示持有，0 表示没有持有）
状态转移方程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k-1][1] + prices[i])
            = max(选择reset， 选择sell)
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            = max(选择reset， 选择buy)

# base case 
d[-1][k][0] = 0 
# i从0开始，i=-1意味着还没有开始，这时的利润为0
dp[-1][k][1] = -infinity
# 还没开始的时候，不可能持有股票，用负无穷表示不可能
dp[i][0][0] = 0
# k从1开始，k=0意味着不允许交易，这时的利润为0
dp[i][0][1] = -infinity 
# 不允许交易的情况下，不可能持有股票，用负无穷表示不可能
==============================
dp[i][k][0]:「状态」有三个，第一个是天数，第二个是当天允许交易的最大次数，第三个是当前的持有状态（即之前说的 rest 的状态，我们不妨用 1 表示持有，0 表示没有持有）
base case
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity 
状态转移方程
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k-1][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # k = 1
        # base case
        # d[-1][0] = dp[i][0] = 0
        # dp[-1][1] = dp[i][1] = -infinity 
        # dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
        # dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for i in range(2)] for _ in range(n)]
        for i in range(0, n):
            if i - 1 == -1:
                # dp[i][0] = max(dp[-1][0], dp[-1][1] + prices[i])
                dp[i][0] = 0
                # dp[i][1] = max(dp[-1][1], -prices[i])
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1],  -prices[i])
        return dp[n-1][0]
    def maxProfit_k_1(self, prices):
        if not prices:
            return 0
        dp_i_0, dp_i_1 = 0, float('-inf')
        n = len(prices)
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        
        return dp_i_0
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [7,1,5,3,6,4]
        res = 5
        self.assertEqual(res, Solution().maxProfit_k_1(s))
    def test_1(self):
        s = [7,6,4,3,1]
        res = 0
        self.assertEqual(res, Solution().maxProfit_k_1(s))
    def test_2(self):
        s = [2,1,4]
        res = 3
        self.assertEqual(res, Solution().maxProfit_k_1(s))

if __name__ == '__main__':
    unittest.main()
    
