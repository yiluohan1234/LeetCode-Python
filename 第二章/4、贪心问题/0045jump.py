#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月28日
#    > description: 
#######################################################################
'''
[45. 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/)
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
'''
import unittest
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        self.memo = [n for _ in range(n)]
        return self.dp(nums, 0)
        
    def dp(self, nums, p):
        n = len(nums)
        if p >= n - 1:
            return 0
        if self.memo[p] != n:
            return self.memo[p]
        steps = nums[p]
        for i in range(1, steps+1):
            subproblem = self.dp(nums, p+i)
            self.memo[p] = min(self.memo[p], 1+subproblem)
        
        return self.memo[p]
    def jump1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心选择性质，我们不需要「递归地」计算出所有选择的具体结果然后比较求最值，而只需要做出那个最有「潜力」，看起来最优的选择即可。
        # i和end标记了可以选择的跳跃步数，farthest标记了所有可选择跳跃步数[i..end]中能够跳到的最远距离，jumps记录了跳跃次数
        n = len(nums)
        if n == 1:
            return 0
        end = 0
        farthest = 0
        jumps = 0
        for i in range(n):
            farthest = max(nums[i] + i, farthest)
            if farthest >= n - 1:
                return jumps + 1
            if end == i:
                jumps += 1
                end = farthest
        return jumps

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [2,3,1,1,4]
        res = 2
        self.assertEqual(res, Solution().jump2(s))
    def test_1(self):
        s = [2,3,0,1,4]
        res = 2
        self.assertEqual(res, Solution().jump2(s))

if __name__ == '__main__':
    unittest.main()