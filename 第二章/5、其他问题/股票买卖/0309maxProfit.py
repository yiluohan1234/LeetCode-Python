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
[309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

示例:
输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''
import unittest
class Solution(object):
    def maxProfit_with_cool(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # dp[-1][k][0] = dp[i][0][0] = 0
        # dp[-1][0][1] = dp[i][0][1] = -inf
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        # dp[-1][0] = dp[i][0] = 0
        # dp[-1][1] = dp[i][1] = -inf
        # k = +infinity with cooldown
        if not prices:
            return 0
        n = len(prices)
        dp_i_0, dp_i_1, dp_pre_i_0 = 0, float('-inf'), 0
        for i in range(0, n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_i_0 - prices[i])
            dp_pre_i_0 = temp
        
        return dp_i_0
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [1,2,3,0,2]      
        res = 3
        self.assertEqual(res, Solution().maxProfit_with_cool(s))
    

if __name__ == '__main__':
    unittest.main()
    
