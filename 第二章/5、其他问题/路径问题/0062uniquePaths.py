#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0062uniquePaths.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/04 16:50:30
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
62. 不同路径(https://leetcode-cn.com/problems/unique-paths/)
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
'''
import unittest
class Solution(object):
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.memo = {}
        return self.dp(m, n, 0, 0)
            
    
    def dp(self, m, n, i, j):
        # 从(i, j)到(m, n)的路径数
        if i == m-1 or j == n-1:
            return 1
        if i > m - 1 or j > n - 1:
            return 0
        if i == m - 1 and j == n - 1:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i,j)]
        #dp[i][j] = dp[i+1][j] + dp[i][j+1]
        res = self.dp(m, n, i+1, j) + self.dp(m, n, i, j+1)
        self.memo[(i,j)] = res
        return res
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j]=x:从(0,0)到(i,j)有x个路径
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j]=x:从(i,j)出发有x个路径
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m-2, -1, -1):
            dp[i][n-1] = dp[i+1][n-1]
        for j in range(n-2, -1, -1):
            dp[m-1][j] = dp[m-1][j+1]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        m = 3
        n = 7
        res = 28
        self.assertEqual(res, Solution().uniquePaths(m, n))
    def test_1(self):
        m = 3
        n = 2
        res = 3
        self.assertEqual(res, Solution().uniquePaths(m, n))
    def test_2(self):
        m = 3
        n = 3
        res = 6
        self.assertEqual(res, Solution().uniquePaths(m, n))
    def test_1(self):
        m = 7
        n = 3
        res = 28
        self.assertEqual(res, Solution().uniquePaths(m, n))

if __name__ == '__main__':
    unittest.main()
    
