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
