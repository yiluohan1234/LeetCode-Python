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
312. 戳气球(https://leetcode-cn.com/problems/burst-balloons/)
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
求所能获得硬币的最大数量。

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

'''
import unittest
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        points = [1]
        for i in range(len(nums)):
            points.append(nums[i])
        points.append(1)
        # 1->n,0和n+1是虚拟气球
        # dp[i][j] = x表示，戳破气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数为x
        # 题目要求的结果就是dp[0][n+1]的值，而 base case 就是dp[i][j] = 0，其中0 <= i <= n+1, j <= i+1
        # 最终状态就是指题目要求的结果，对于这道题目也就是dp[0][n+1]。
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        # 「状态」和「选择」：i和j就是两个「状态」，最后戳破的那个气球k就是「选择」
        # 确定遍历方向：base， 重点，需要的子状态
        for i in range(n, -1, -1):
            for j in range(i+1, n+2):
                # 最后戳破的气球是哪个？
                for k in range(i+1, j):
                    # 根据刚才对dp数组的定义，如果最后一个戳破气球k，dp[i][j]的值应该为：
                    # 你不是要最后戳破气球k吗？那得先把开区间(i, k)的气球都戳破，再把开区间(k, j)的气球都戳破；
                    # 最后剩下的气球k，相邻的就是气球i和气球j，这时候戳破k的话得到的分数就是points[i]*points[k]*points[j]。
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i]*points[k]*points[j])
        return dp[0][n + 1]
            
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [3,1,5,8]
        res = 167
        self.assertEqual(res, Solution().maxCoins(nums))
    def test_1(self):
        nums = [1,5]
        res = 10
        self.assertEqual(res, Solution().maxCoins(nums))

if __name__ == '__main__':
    unittest.main()
    
