#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月18日
#    > description: 
#######################################################################
'''
[494. 目标和](https://leetcode-cn.com/problems/target-sum/)
给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

 

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

子集划分问题是一个典型的背包问题。
背包问题的基本形式：
有一个背包，容量为 sum，现在给你 N 个物品，第 i 个物品的重量为 nums[i - 1]（注意 1 <= i <= N），
每个物品只有一个，请问你有几种不同的方法能够恰好装满这个背包？
1、明确状态。「背包的容量」和「可选择的物品」
2、定义 dp 数组/函数的含义。dp[i][j] = x 表示，若只在前 i 个物品中选择，若当前背包的容量为 j，则最多有 x 种方法可以恰好装满背包。
3、明确「选择」并择优。「装进背包」或者「不装进背包」
4、明确 base case。根据这个定义，显然 dp[0][..] = 0，因为没有物品的话，根本没办法装背包；dp[..][0] = 1，因为如果背包的最大载重为 0，「什么都不装」就是唯一的一种装法。
我们要求的答案：dp[N][sum]，即使用所有 N 个物品，有几种方法可以装满容量为 sum 的背包。

根据「选择」，思考状态转移的逻辑，即状态转移方程。
如果不把 nums[i] 算入子集，或者说你不把这第 i 个物品装入背包，那么恰好装满背包的方法数就取决于上一个状态 dp[i-1][j]，继承之前的结果。
如果把 nums[i] 算入子集，或者说你把这第 i 个物品装入了背包，那么只要看前 i - 1 个物品有几种方法可以装满 j - nums[i-1] 的重量就行了，所以取决于状态 dp[i-1][j-nums[i-1]]。
由于 dp[i][j] 为装满背包的总方法数，所以应该以上两种选择的结果求和，得到状态转移方程。
dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
'''
import unittest
class Solution(object):
    def __init__(self):
        self.memo = {}
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 伪代码思路
        # def backtrack(nums, i):
        # if i == len(nums):
        #     if 达到 target:
        #         result += 1
        #     return
        # for op in { +1, -1 }:
        #     选择 op * nums[i]
        #     # 穷举 nums[i + 1] 的选择
        #     backtrack(nums, i + 1)
        #     撤销选择
        if len(nums) == 0:
            return 0
        self.res = 0
        self.backtrack(nums, 0, target)
        return self.res
    def backtrack(self, nums, i, rest):
        if i == len(nums):
            if rest == 0:
                self.res += 1
            return 
        # '+'
        rest -= nums[i]
        self.backtrack(nums, i+1, rest)
        rest += nums[i]
        # '-'
        rest += nums[i]
        self.backtrack(nums, i+1, rest)
        rest -= nums[i]
    def findTargetSumWays1(self, nums, target):
        # 回溯算法
        if len(nums) == 0:
            return 0
        res = self.backtrack1(nums, 0, target)
        return res
    def backtrack1(self, nums, i, rest):
        if i == len(nums):
            if rest == 0:
                return 1
            return 0
        
        result = self.backtrack1(nums, i+1, rest-nums[i]) + self.backtrack1(nums, i+1, rest+nums[i])
        return result
    def findTargetSumWays2(self, nums, target):
        # 带备忘录的回溯算法
        if len(nums) == 0:
            return 0
        res = self.dp(nums, 0, target)
        return res
    def dp(self, nums, i, rest):
        if i == len(nums):
            if rest == 0:
                return 1
            return 0
        if (i, rest) in self.memo:
            return self.memo[(i, rest)]
        result = self.dp(nums, i+1, rest-nums[i]) + self.dp(nums, i+1, rest+nums[i])
        self.memo[(i, rest)] = result
        return result
    def findTargetSumWays3(self, nums, target):
        # 动态规划
        # nums划分为子集 A 和 B，分别代表分配 + 的数和分配 - 的数
        # 则 sum(A) - sum(B) = target => sum(A) = target + sum(B) => 2*sum(A) = target+sum(B)+sum(A) => 2*sum(A)=target+sum(nums)
        # 把原问题转化成：nums 中存在几个子集 A，使得 A 中元素的和为 (target + sum(nums)) / 2
        sum_nums = 0
        for num in nums:
            sum_nums += num
        # python可以直接用sum函数
        #sum_nums = sum(nums)
        if sum_nums < target or (sum_nums + target) % 2 == 1:
            return 0
        return self.subsets1(nums, (target+sum_nums)//2)
    
    def subsets(self, nums, target):
        #1、状态：放进背包和不放进背包
        n = len(nums)
        #2、定义：dp[i][j] = x,若在前i物品中选择，背包容量为j，则最多有x种方法装进背包
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(0, target+1):                                                                                                                                                        
                #3、选择：
                #不把num[i]放入背包，装满背包取决于上一个状态dp[i-1][j]
                #把nums[i]放入背包，装满背包取决于前 i-1个物品有几种方法可以装满 j-nums[i-1]的重量就行了
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    # 背包的空间不足，只能选择不装物品 i
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target]
    def subsets1(self, nums, target):
        #1、状态：放进背包和不放进背包
        n = len(nums)
        #2、定义：dp[i][j] = x,若在前i物品中选择，背包容量为j，则最多有x种方法装进背包
        dp = [0 for _ in range(target+1)] 
        dp[0] = 1 #《漫画算法》和《码农翻身》
        # 对照二维 dp，只要把 dp 数组的第一个维度全都去掉就行了，唯一的区别就是这里的 j 要从后往前遍历，原因如下：
        # 因为二维压缩到一维的根本原理是，dp[j] 和 dp[j-nums[i-1]] 还没被新结果覆盖的时候，相当于二维 dp 中的 dp[i-1][j] 和 dp[i-1][j-nums[i-1]]。
        # 那么，我们就要做到：在计算新的 dp[j] 的时候，dp[j] 和 dp[j-nums[i-1]] 还是上一轮外层 for 循环的结果。
        # 如果你从前往后遍历一维 dp 数组，dp[j] 显然是没问题的，但是 dp[j-nums[i-1]] 已经不是上一轮外层 for 循环的结果了，这里就会使用错误的状态，当然得不到正确的答案
        for i in range(1, n+1):
            for j in range(target, -1, -1):
                #3、选择：
                #不把num[i]放入背包，装满背包取决于上一个状态dp[i-1][j]
                #把nums[i]放入背包，装满背包取决于前 i-1个物品有几种方法可以装满 j-nums[i-1]的重量就行了
                if j >= nums[i-1]:
                    dp[j] = dp[j] + dp[j-nums[i-1]]
                else:
                    # 背包的空间不足，只能选择不装物品 i
                    dp[j] = dp[j]
        
        return dp[target]
            
        
        
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1,1,1,1,1]
        target = 3
        res = 5
        self.assertEqual(res, Solution().findTargetSumWays(nums, target))

if __name__ == "__main__":
    unittest.main()