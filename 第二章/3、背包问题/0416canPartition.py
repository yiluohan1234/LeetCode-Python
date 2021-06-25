#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月26日
#    > description: 
#######################################################################
'''
[416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。


'''
import unittest
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 给N个物品和一个可装载重量为sum/2的背包，每个物品的重量为nums[i]。现在让你装物品，是否存在一种装法，能够恰好将背包装满？
        # 1、状态与选择：背包容量和可选择的物品；装进背包或不装进背包
        sum_nums = sum(nums)
        n = len(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2
        # 2、dp[i][j]定义：dp[i][j] = x表示，对于前i个物品，当前背包的容量为j时，若x为true，则说明可以恰好将背包装满，若x为false，则说明不能恰好将背包装满
        dp =[[False for _ in range(target + 1)] for _ in range(n+1)]
        # 3、根据定义：最终答案为dp[n][target], base case如下
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, target+1):
                if j - nums[i-1] >= 0:
                    # 4、根据选择，思考状态转移方程
                    # 如果不把这第i个物品装入背包：那么是否能够恰好装满背包，取决于上一个状态 dp[i-1][j]，继承之前的结果。
                    # 如果把第i个物品装入了背包：那么是否能够恰好装满背包，取决于状态 dp[i - 1][j-nums[i-1]]。
                    # 注：由于i是从 1 开始的，而数组索引是从 0 开始的，所以第i个物品的重量应该是nums[i-1]。
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j] 
        
        return dp[n][target]

    def canPartition1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        n = len(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2
        dp =[False for _ in range(target + 1)]
        #base
        for i in range(n+1):
            dp[0] = True
        for i in range(1, n+1):
            for j in range(target, 0, -1):
                if j - nums[i-1] >= 0:
                    dp[j] = dp[j] or dp[j-nums[i-1]]
        
        return dp[target]
                    
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1,5,11,5]
        res = True
        self.assertEqual(res, Solution().canPartition1(nums))
    def test_1(self):
        nums = [1,2,3,5]
        res = False
        self.assertEqual(res, Solution().canPartition1(nums))

if __name__ == '__main__':
    unittest.main()