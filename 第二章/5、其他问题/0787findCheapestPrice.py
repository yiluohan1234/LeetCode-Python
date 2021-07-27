#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0787findCheapestPrice.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/26 09:30:51
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
787. K 站中转内最便宜的航班(https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/)
有 n 个城市通过 m 个航班连接。每个航班都从城市 u 开始，以价格 w 抵达 v。
现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到从 src 到 dst 最多经过 k 站中转的最便宜的价格。 如果没有这样的路线，则输出 -1。
'''
import unittest
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # 将k次改为k条边
        k += 1
        self.src = src 
        self.indegree = {}
        self.memo = {}
        for f in flights:
            f_start= f[0]
            f_end = f[1]
            prices = f[2]
            self.indegree.setdefault(f_end, {})[f_start] = prices
        
        return self.dp(dst, k)

    def dp(self, s, k):
        # 从src 到 s，k个中转的最小费用
        if s == self.src:
            return 0
        
        if k == 0:
            return -1

        if (s, k) in self.memo:
            return self.memo[(s, k)]

        res = float('inf')
        # 首先s要在self.indegree
        if s in self.indegree:
            for f_points, prices in self.indegree[s].items():
                sub_problem = self.dp(f_points, k-1)
                if sub_problem != -1:
                    res = min(res, sub_problem + prices)
        
        self.memo[(s, k)] = -1 if res == float('inf') else res 

        return self.memo[(s, k)]
        
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 1
        res = 200
        self.assertEqual(res, Solution().findCheapestPrice(n, flights, src, dst, k))
    def test_1(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 0
        res = 500
        self.assertEqual(res, Solution().findCheapestPrice(n, flights, src, dst, k))

if __name__ == '__main__':
    unittest.main()
    
