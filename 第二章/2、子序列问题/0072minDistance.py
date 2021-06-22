#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月19日
#    > description: 
#######################################################################
'''
[72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
 

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解决两个字符串的动态规划问题，一般都是用两个指针i,j分别指向两个字符串的最后，然后一步步往前走，缩小问题的规模。

base case 是i走完s1或j走完s2，可以直接返回另一个字符串剩下的长度。
def dp(i, j) -> int
# 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离

对于每对儿字符s1[i]和s2[j]，可以有四种操作：
if s1[i] == s2[j]:
    啥都别做（skip）
    i, j 同时向前移动
else:
    三选一：
        插入（insert）
        删除（delete）
        替换（replace）
if s1[i] == s2[j]:
    return dp(i - 1, j - 1)  # 啥都不做
    # 解释：
    # 本来就相等，不需要任何操作
    # s1[0..i] 和 s2[0..j] 的最小编辑距离等于
    # s1[0..i-1] 和 s2[0..j-1] 的最小编辑距离
    # 也就是说 dp(i, j) 等于 dp(i-1, j-1)
如果s1[i]！=s2[j]，就要对三个操作递归了，稍微需要点思考:
    1、dp(i, j - 1) + 1,    # 插入
    # 解释：
    # 我直接在 s1[i] 插入一个和 s2[j] 一样的字符
    # 那么 s2[j] 就被匹配了，前移 j，继续跟 i 对比
    # 别忘了操作数加一
    2、dp(i - 1, j) + 1,    # 删除
    # 解释：
    # 我直接把 s[i] 这个字符删掉
    # 前移 i，继续跟 j 对比
    # 操作数加一
    3、dp(i - 1, j - 1) + 1 # 替换
    # 解释：
    # 我直接把 s1[i] 替换成 s2[j]，这样它俩就匹配了
    # 同时前移 i，j 继续对比
    # 操作数加一
这个方法存在重叠子问题，怎么看出来的？  抽象出本文算法的递归框架
def dp(i, j):
    dp(i - 1, j - 1) #1
    dp(i, j - 1)     #2
    dp(i - 1, j)     #3
对于子问题dp(i-1,j-1)，如何通过原问题dp(i,j)得到呢？
有不止一条路径，比如dp(i,j)->#1和dp(i,j)->#2->#3。一旦发现一条重复路径，就说明存在巨量重复路径，也就是重叠子问题。
'''
import unittest
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def dp(i, j):
            if i == -1:return j + 1
            if j == -1:return i + 1
            
            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(
                    dp(i, j - 1) + 1,
                    dp(i - 1, j) + 1,
                    dp(i - 1, j - 1) + 1
                    )
        
        return dp(len(word1) - 1, len(word2) - 1)
    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            if i == -1:return j + 1
            if j == -1:return i + 1
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = min(
                    dp(i, j - 1) + 1,
                    dp(i - 1, j) + 1,
                    dp(i - 1, j - 1) + 1
                    )
            return memo[(i, j)]
        
        return dp(len(word1) - 1, len(word2) - 1)
    
    def minDistance2(self, s1, s2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j 
        for i in range(1, m+1):
            for j in range(1, n + 1):
                # def dp(i, j) -> int
                # 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
                # dp[i-1][j-1]
                # 存储 s1[0..i] 和 s2[0..j] 的最小编辑距离
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i][j-1] + 1,
                        dp[i-1][j] + 1,
                        dp[i-1][j-1] + 1
                        )
        return dp[m][n]
        
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        word1 = "horse"
        word2 = "ros"
        res = 3
        self.assertEqual(res, Solution().minDistance2(word1, word2))
    def test_1(self):
        word1 = "intention"
        word2 = "execution"
        res = 5
        self.assertEqual(res, Solution().minDistance2(word1, word2))

if __name__ == "__main__":
    unittest.main()
