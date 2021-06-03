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
198. 打家劫舍(https://leetcode-cn.com/problems/house-robber/)
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''
import unittest
class Solution(object):
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 解决动态规划问题就是找「状态」和「选择」，仅此而已
        # 选择：抢或者不抢,状态：房子的索引
        self.memo = [-1 for _ in range(len(nums))]
        return self.dp(nums, 0)
    
    def dp1(self, nums, start):
        if start >= len(nums):
            return 0
        res = max(
                self.dp(nums, start+1),
                nums[start] + self.dp(nums, start+2)
            )
        return res
    def dp(self, nums, start):
        if start >= len(nums):
            return 0
        if self.memo[start] != -1:
            return self.memo[start]
        res = max(
                self.dp(nums, start+1),
                nums[start] + self.dp(nums, start+2)
            )
        self.memo[start] = res
        return res
    def rob2(self, nums):
        n = len(nums)
        # dp[i] = x 表示：从第 i 间房子开始抢劫，最多能抢到的钱为 x 
        # base case: dp[n] = 0
        # 思考??? 状态转移只和dp[i]最近的两个状态有关
        dp = [0 for _ in range(n+2)]
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        
        return dp[0]
    def rob(self, nums):
        n = len(nums)
        # 记录 dp[i+1] 和 dp[i+2]
        dp_i_1, dp_i_2 = 0, 0
        # 记录 dp[i]
        dp_i = 0
        for i in range(n-1, -1, -1):
            dp_i = max(dp_i_1, nums[i] + dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
            
        return dp_i
       
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [1,2,3,1]
        res = 4
        self.assertEqual(res, Solution().rob(s))
    def test_1(self):
        s = [2,7,9,3,1]
        res = 12
        self.assertEqual(res, Solution().rob(s))

if __name__ == '__main__':
    unittest.main()
    
