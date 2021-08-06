#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0063uniquePathsWithObstacles.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/05 10:00:08
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
63. 不同路径 II(https://leetcode-cn.com/problems/unique-paths-ii/)
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
'''
import unittest
class Solution(object):
    def uniquePathsWithObstacles1(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp[i][j]=x:从(i,j)出发有x个路径
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1 if obstacleGrid[m-1][n-1] == 0 else 0
        for i in range(m-2, -1, -1):
            if obstacleGrid[i][n-1] == 0:
                dp[i][n-1] = dp[i+1][n-1]
        for j in range(n-2, -1, -1):
            if obstacleGrid[m-1][j] == 0:
               dp[m-1][j] = dp[m-1][j+1]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp[i][j]=x:从(0,0)到(i,j)有x个路径
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
               dp[0][j] = dp[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        res = 2
        self.assertEqual(res, Solution().uniquePathsWithObstacles(obstacleGrid))
    def test_1(self):
        obstacleGrid = [[0,1],[0,0]]
        res = 1
        self.assertEqual(res, Solution().uniquePathsWithObstacles(obstacleGrid))

if __name__ == '__main__':
    unittest.main()
    
