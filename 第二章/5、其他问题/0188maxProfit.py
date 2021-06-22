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
188. 买卖股票的最佳时机 IV(https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

'''
import unittest
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[[0 for i in range(2)] for _ in range(k+1)] for _ in range(n)]
        if k > n / 2:
            return self.maxProfit_k_inf(prices)
        for i in range(n):
            for k in range(k, 0, -1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[n-1][k][0]
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
        k = 2
        prices = [2,4,1]
        res = 2
        self.assertEqual(res, Solution().maxProfit(k, prices))
    def test_1(self):
        k = 2
        prices = [3,2,6,5,0,3]
        res = 7
        self.assertEqual(res, Solution().maxProfit(k, prices))
    

if __name__ == '__main__':
    unittest.main()
    
