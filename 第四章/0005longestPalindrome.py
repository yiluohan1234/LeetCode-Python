#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月11日
#    > description: 
#######################################################################
'''
[5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)
给你一个字符串 s，找到 s 中最长的回文子串。

'''
import unittest
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(0, len(s)):
            # 找到以 s[i] 为中心的回文串
            s1 = self.palinderome(s, i, i)
            s2 = self.palinderome(s, i, i+1)
            # 找到以 s[i] 和 s[i+1] 为中心的回文串
            res = res if len(res) >= len(s1) else s1
            res = res if len(res) >= len(s2) else s2
        return res
    def palinderome(self, s, l, r):
        # 以l,r为中心的最长回文串,可以同时处理回文串长度为奇数和偶数
        while l >= 0 and r < len(s) and s[r] == s[l]:
            l -= 1
            r += 1
        return s[l+1:r]
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "babad"
        res = "bab"
        self.assertEqual(res, Solution().longestPalindrome(s))

if __name__ == "__main__":
    unittest.main()
