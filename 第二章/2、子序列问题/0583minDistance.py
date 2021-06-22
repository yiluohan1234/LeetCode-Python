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
[583. 两个字符串的删除操作](https://leetcode-cn.com/problems/delete-operation-for-two-strings/)
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例：
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
 

提示：
给定单词的长度不超过500。
给定单词中的字符只含有小写字母。

'''
import unittest
class Solution(object):
    def minDistance(self, s1, s2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        lcs = self.longestCommonSubsequence(s1, s2);
        return m - lcs + n - lcs;
    def longestCommonSubsequence(self, s1, s2):
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
        text1 = "sea"
        text2 = "eat"
        res = 2
        self.assertEqual(res, Solution().minDistance(text1, text2))
    

if __name__ == "__main__":
    unittest.main()
