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

其核心思路是在二维 dp 的基础上使用元组分别存储两个人的博弈结果。
掌握了这个技巧以后，别人再问你什么俩海盗分宝石，俩人拿硬币的问题，你就告诉别人：我懒得想，直接给你写个算法算一下得了。
博弈问题的难点在于，两个人要轮流进行选择，而且都贼精明，应该如何编程表示这个过程呢？

dp[i][j][0] = max(piles[i] +dp[i+1][j][1], piles[j] + dp[i][j-1][1])
            = (选择最左边的石头堆， 选择最右边的石头堆)
我最为先手，面对pile[i..j]时，有两种选择：
选择最左边的，然后面对piles[i+1, j]，但此时轮到对方，我变成后手。
选择最右边的，然后面对piles[i, j-1]，但此时轮到对方，我变成后手。
if 先手选择左边：
    dp[i][j][1] = dp[i+1][j][0]
if 先手选择右边：
    dp[i][j][1] = dp[i][j-1][0]
我作为后手，要等先手先选择：
如果先手选择了左边，给我剩下了piles[i+1, j]，但此时轮到我，我变成先手。
如果先手选择了右边，给我剩下了piles[i, j-1]，但此时轮到我，我变成先手。
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
            # dp[i][j][0]: 对于piles[i..j]这部分石碓，先手获得的最高分数
            # dp[i][j][1]: 对于piles[i..j]这部分石碓，后手获得的最高分数
            # 我们想获得的答案就是：dp[0][n-1][0] -dp[0][n-1][1]
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
