#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月1日
#    > description: 
#######################################################################
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
        return dp[0][n - 1];
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
        s = "babad"
        res = "bab"
        self.assertEqual(res, Solution().longestPalindrome(s))

if __name__ == '__main__':
    unittest.main()