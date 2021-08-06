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
[714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 price    s[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
'''
import unittest
class Solution(object):
    def maxProfit_with_fee(self, prices, fee):
        """
        :type prices: List[int]
        :rtype: int
        """
        # k = +infinity with fee
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # dp[-1][k][0] = dp[i][0][0] = 0
        # dp[-1][0][1] = dp[i][0][1] = -inf
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i] - fee)
        # dp[-1][0] = dp[i][0] = 0
        # dp[-1][1] = dp[i][1] = -inf
        if not prices:
            return 0
        dp_i_0, dp_i_1 = 0, float('-inf')
        n = len(prices)
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)
        
        return dp_i_0
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        res = 8
        self.assertEqual(res, Solution().maxProfit_with_fee(prices, fee))

if __name__ == '__main__':
    unittest.main()
    
