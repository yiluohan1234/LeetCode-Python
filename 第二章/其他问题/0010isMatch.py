#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月31日
#    > description: 
#######################################################################
'''
10. 正则表达式匹配(https://leetcode-cn.com/problems/regular-expression-matching/)
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

'''
import unittest
class Solution(object):
    def isMatch2(self, s, p):
        if not p:
            return not s 
        first_match = len(s) > 0 and p[0] in (s[0], '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch2(s, p[2:]) or first_match and self.isMatch2(s[1:], p)
        else:
            return first_match and self.isMatch2(s[1:], p[1:])
    def isMatch1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def dfs(s, p):
            if (s, p) in memo:
                return memo[(s, p)]
            if not p:
                return not s 
            first_match = len(s) > 0 and p[0] in (s[0], '.')
            if len(p) >= 2 and p[1] == '*':
                memo[(s, p)] = dfs(s, p[2:]) or first_match and dfs(s[1:], p)
            else:
                memo[(s, p)] = first_match and dfs(s[1:], p[1:])
            return memo[(s,p)]
        return dfs(s, p)
    def isMatch(self, s, p):
        memo = {}
        def dp(i, j):
            if (i, j) in memo:return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            first = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p) - 2 and p[j+1] == '*':
                ans = dp(i, j+2) or first and dp(i+1, j)
            else:
                ans = first and dp(i+1, j+1)
            
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "aab" 
        p = "c*a*b"
        res = True
        self.assertEqual(res, Solution().isMatch2(s, p))

    def test_1(self):
        s = "mississippi" 
        p = "mis*is*p*."
        res = False
        self.assertEqual(res, Solution().isMatch2(s, p))
    def test_2(self):
        s = "ab" 
        p = ".*"
        res = True
        self.assertEqual(res, Solution().isMatch2(s, p))

    def test_3(self):
        s = "aa" 
        p = "a*"
        res = True
        self.assertEqual(res, Solution().isMatch2(s, p))
    def test_4(self):
        s = "aa" 
        p = "a"
        res = False
        self.assertEqual(res, Solution().isMatch2(s, p))
if __name__ == '__main__':
    unittest.main()