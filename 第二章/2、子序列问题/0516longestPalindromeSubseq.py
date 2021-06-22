#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月17日
#    > description: 
#######################################################################
'''
[516. 最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence/)
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000。

'''
import unittest
class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        # dp 数组全部初始化为 0
        # dp 数组的定义：在子串s[i..j]中，最长回文子序列的长度为dp[i][j]。
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # base case
        for i in range(n):
            dp[i][i] = 1
        # 反着遍历保证正确的状态转移
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # 状态转移方程
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # 整个 s 的最长回文子串长度
        return dp[0][n - 1];
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "bbbab"
        res = 4
        self.assertEqual(res, Solution().longestPalindromeSubseq(s))
    def test_1(self):
        s = "cbbd"
        res = 2
        self.assertEqual(res, Solution().longestPalindromeSubseq(s))

if __name__ == '__main__':
    unittest.main()
    
