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
123. 买卖股票的最佳时机 III(https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 
示例 1:
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
'''
import unittest
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # k = 2
        n = len(prices)
        k_max = 2
        dp = [[[0 for i in range(2)] for _ in range(k_max+1)] for _ in range(n)]
        for i in range(n):
            for k in range(k_max, 0, -1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[n-1][k_max][0]
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [3,3,5,0,0,3,1,4]
        res = 6
        self.assertEqual(res, Solution().maxProfit(s))
    

if __name__ == '__main__':
    unittest.main()
    
