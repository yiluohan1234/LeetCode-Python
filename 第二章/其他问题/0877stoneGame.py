#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月1日
#    > description: 
#######################################################################
'''
[877. 石子游戏](https://leetcode-cn.com/problems/stone-game/)
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。
'''
import unittest
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # 状态显然有三个：开始的索引 i，结束的索引 j，当前轮到的人
        # 选择有两个：选择最左边的那堆石头，或者选择最右边的那堆石头
        n = len(piles)
        dp = [[[0,0] for _ in range(n)] for _ in range(n)]
        # base
        for i in range(n):
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                left = piles[i] +dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]
        res= dp[0][n-1]
        return res[0] - res[1]
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [5,3,4,5]
        res = True
        self.assertEqual(res, Solution().stoneGame(s))

if __name__ == "__main__":
    unittest.main()
