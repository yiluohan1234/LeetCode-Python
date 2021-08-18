#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 1312minInsertions.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/27 13:31:43
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
[1312. 让字符串成为回文串的最少插入次数](https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)
给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
请你返回让 s 成为回文串的 最少操作次数 。
「回文串」是正读和反读都相同的字符串。
'''
import unittest
class Solution(object):
    def minInsertions0(self, s):
        n = len(s)
        # 定义：对 s[i..j]，最少需要插入 dp[i][j] 次才能变成回文
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # base case：i == j 时 dp[i][j] = 0，单个字符本身就是回文
        # dp 数组已经全部初始化为 0，base case 已初始化
        
        # 状态转移就是从小规模问题的答案推导更大规模问题的答案
        # 从下向上遍历
        for i in range(n-2, -1, -1):
            # 从左向右遍历
            for j in range(i+1, n):
                # 根据 s[i] 和 s[j] 进行状态转移
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
                

        # 根据 dp 数组的定义，题目要求的答案
        return dp[0][n - 1]
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n)]

        temp = 0
        for i in range(n-2, -1, -1):
            # 记录dp[i+1][j-1]
            pre = 0
            for j in range(i+1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    # dp[i][j] = dp[i+1][j-1]
                    dp[j] = pre
                else:
                    # dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
                    dp[j] = min(dp[j], dp[j-1]) + 1
                
                pre = temp
        
        return dp[n-1]
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "zzazz"
        res = 0
        self.assertEqual(res, Solution().minInsertions0(s))
    def test_1(self):
        s = "mbadm"
        res = 2
        self.assertEqual(res, Solution().minInsertions0(s))
    def test_2(self):
        s = "leetcode"
        res = 5
        self.assertEqual(res, Solution().minInsertions0(s))
    def test_3(self):
        s = "g"
        res = 0
        self.assertEqual(res, Solution().minInsertions0(s))
    def test_4(self):
        s = "no"
        res = 1
        self.assertEqual(res, Solution().minInsertions0(s))

if __name__ == '__main__':
    unittest.main()