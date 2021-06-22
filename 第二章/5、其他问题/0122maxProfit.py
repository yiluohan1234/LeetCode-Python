#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月2日
#    > description: 
#######################################################################
'''
122. 买卖股票的最佳时机 II(https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
     
dp[i][k][0]:「状态」有三个，第一个是天数，第二个是当天允许交易的最大次数，第三个是当前的持有状态（即之前说的 rest 的状态，我们不妨用 1 表示持有，0 表示没有持有）
base case
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity 
状态转移方程(k 为正无穷，那么就可以认为 k 和 k - 1 是一样的)
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k-1][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
'''
import unittest
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # k = +infinity
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        for i in range(n):
            if i-1 == -1:
                dp[i][1] = -prices[i] # max(dp[-1][1], dp[-1][0] - prices[i])
                dp[i][0] = 0 # max(dp[-1][0], dp[-1][1] + prices[i])
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]
    def maxProfit_k_inf(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [7,1,5,3,6,4]
        res = 7
        self.assertEqual(res, Solution().maxProfit_k_inf(s))
    def test_1(self):
        s = [1,2,3,4,5]
        res = 4
        self.assertEqual(res, Solution().maxProfit_k_inf(s))
    def test_2(self):
        s = [7,6,4,3,1][3,2,6,5,0,3]
        res = 0
        self.assertEqual(res, Solution().maxProfit_k_inf(s))


if __name__ == '__main__':
    unittest.main()
    
