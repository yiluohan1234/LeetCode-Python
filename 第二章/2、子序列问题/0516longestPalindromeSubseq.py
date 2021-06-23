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

子序列模板：
1、一维dp数组
n = len(array)
dp = [0 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        dp[i] = 最值(dp[i], dp[j] + ...)
以 最长递增子序列为例 ，在子数组array[0..i]中，以array[i]结尾的目标子序列（最长递增子序列）的长度是dp[i]。
2、二维dp数组
n = len(arr)
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(1, n):
        if arr[i] == arr[j]: 
            dp[i][j] = dp[i][j] + ...
        else:
            dp[i][j] = 最值(...)

这种思路运用相对更多一些，尤其是涉及两个字符串/数组的子序列。
2.1 涉及两个字符串/数组时
dp 数组的含义：在子数组arr1[0..i-1]和子数组arr2[0..j-1]中，我们要求的子序列（最长公共子序列）长度为dp[i][j]。
m, n = len(arr1), len(arr2)
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if arr1[i-1] == arr2[j-1]: 
            dp[i][j] = dp[i][j] + ...
        else:
            dp[i][j] = 最值(...)
2.2 只涉及一个字符串/数组时
dp 数组的含义：在子数组array[i..j]中，我们要求的子序列（最长回文子序列）的长度为dp[i][j]。
n = len(array)
dp = [0 for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if s[i] == s[j]:
            dp[i][j] = dp[i + 1][j - 1] + ...
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
return dp[0][n - 1]
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
    
