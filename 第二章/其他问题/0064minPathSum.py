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
[64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：
1    3    1
1    5    1
4    2    1

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
'''
import unittest
class Solution(object):
    def __init__(self):
        self.memo = {}
    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # dp:从左上角位置 (0, 0) 走到位置 (i, j) 的最小路径和为 dp(grid, i, j)
        return self.dp(grid, m-1, n-1)
    
    def dp(self, grid , i, j):
        if (i,j) in self.memo:
            return self.memo[(i,j)]
        # base case
        if i == 0 and j == 0:
            return grid[0][0]

        # 如果索引出界，返回一个很大的值，保证在取 min 的时候不会被取到
        if i < 0 or j < 0:
            return float('inf')
        
        res = min(
            self.dp(grid, i-1, j),
            self.dp(grid, i, j-1)
        ) + grid[i][j]
        self.memo[(i,j)] = res
        return res
        # 判断重叠子问题
        # 如果我想从 dp(i, j) 递归到 dp(i-1, j-1)，有几种不同的递归调用路径？
        # int dp(int i, int j) {
        #     dp(i - 1, j); // #1
        #     dp(i, j - 1); // #2
        # }
        # dp[i][j]->#1->#2或dp[i][j]->#2->#1
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # base case
        dp[0][0] = grid[0][0]
        # 那如果 i 或者 j 等于 0 的时候，就会出现索引越界的错误。所以我们需要提前计算出 dp[0][..] 和 dp[..][0]，然后让 i 和 j 的值从 1 开始迭代。
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [[1,3,1],[1,5,1],[4,2,1]]
        res = 7
        self.assertEqual(res, Solution().minPathSum(s))

if __name__ == '__main__':
    unittest.main()
    
