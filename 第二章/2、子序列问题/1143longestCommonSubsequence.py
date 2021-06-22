#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月25日
#    > description: 
#######################################################################
'''
[1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

对于两个字符串求子序列的问题，都是用两个指针i和j分别在两个字符串上移动，大概率是动态规划思路。
dp函数的定义：dp(s1, i, s2, j)计算s1[i..]和s2[j..]的最长公共子序列长度。
base case 就是i == len(s1)或j == len(s2)时，因为这时候s1[i..]或s2[j..]就相当于空串了，最长公共子序列的长度显然是 0.

'''
import unittest
class Solution(object):      
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # dp(s1, i, s2, j)计算s1[i..]和s2[j..]的最长公共子序列长度。
        m, n = len(text1), len(text2)
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dp(text1, 0, text2, 0)
    def dp(self, s1, i, s2, j):
        if i == len(s1) or j == len(s2):
            return 0
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        if s1[i] == s2[j]:
            self.memo[i][j] = 1 + self.dp(s1, i+1, s2, j+1)
        else:
            self.memo[i][j] = max(
                self.dp(s1, i+1, s2, j), # 情况一、s1[i] 不在 lcs 中
                self.dp(s1, i, s2, j+1)  # 情况二、s2[j] 不在 lcs 中
                # 情况三、都不在 lcs 中 
                # self.dp(s1, i + 1, s2, j + 1),可以忽略
            )
        
        return self.memo[i][j]
    def longestCommonSubsequence1(self, s1, s2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 定义：s1[0..i-1] 和 s2[0..j-1] 的 lcs 长度为 dp[i][j]
        # 目标：s1[0..m-1] 和 s2[0..n-1] 的 lcs 长度，即 dp[m][n]
        # base case: dp[0][..] = dp[..][0] = 0
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        text1 = "abc"
        text2 = "abc"
        res = 3
        self.assertEqual(res, Solution().longestCommonSubsequence1(text1, text2))
    def test_1(self):
        text1 = "abc"
        text2 = "def"
        res = 0
        self.assertEqual(res, Solution().longestCommonSubsequence1(text1, text2))
    def test_2(self):
        text1 = "abcde"
        text2 = "ace" 
        res = 3
        self.assertEqual(res, Solution().longestCommonSubsequence1(text1, text2))

if __name__ == "__main__":
    unittest.main()
