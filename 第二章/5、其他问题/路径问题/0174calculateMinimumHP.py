#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月3日
#    > description: 
#######################################################################
'''
[174. 地下城游戏](https://leetcode-cn.com/problems/dungeon-game/)
一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。
我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
为了尽快到达公主，骑士决定每次只向右或向下移动一步。

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
'''
import unittest
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        memo = {}
        m, n = len(dungeon), len(dungeon[0])
        def dp(grid, i, j):
            # 从左上角（grid[0][0]）走到 grid[i][j] 至少需要 dp(grid, i, j) 的生命值。错误的定义
            # 从 grid[i][j] 到达终点（右下角）所需的最少生命值是 dp(grid, i, j)。
            # 定义：从 (i, j) 到达右下角，需要的初始血量至少是多少
            # base case
            m, n = len(grid), len(grid[0])
            # base case
            if i == m-1 and j == n-1:
                return 1 if grid[i][j] >= 0 else -grid[i][j] + 1
            if i == m or j == n:
                return float('inf')
            # 避免重复计算
            if (i,j) in memo:
                return memo[(i,j)]
            # 状态转移逻辑
            res = min(dp(grid, i+1, j), dp(grid, i, j+1)) - grid[i][j]
            # 骑士的生命值至少为 1
            memo[(i,j)] = 1 if res <= 0 else res
            return memo[(i,j)]
        return dp(dungeon, 0, 0)
    
    
    def calculateMinimumHP1(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1 if dungeon[m-1][n-1] > 0 else -dungeon[m-1][n-1] + 1

        for i in range(m-2, -1, -1):
            tmp = dp[i+1][n-1] - dungeon[i][n-1]
            dp[i][n-1] =  tmp if tmp > 0 else 1
        for i in range(n-2, -1, -1):
            tmp = dp[m-1][i+1] - dungeon[m-1][i]
            dp[m-1][i] =  tmp if tmp > 0 else 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                tmp = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = tmp if tmp > 0 else 1

        return dp[0][0]
class TestSolution(unittest.TestCase):
    def test_0(self):
        dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
        res = 7
        self.assertEqual(res, Solution().calculateMinimumHP(dungeon))
    def test_1(self):
        dungeon = [[0]]
        res = 1
        self.assertEqual(res, Solution().calculateMinimumHP(dungeon))

if __name__ == '__main__':
    unittest.main()
    
