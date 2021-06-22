#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月1日
#    > description: 
#######################################################################
'''
[28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)
实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2
'''
import unittest
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        km = KMP(needle)
        res = km.search(haystack)
        return res
    def strStr1(self, haystack, needle):
        if needle not in haystack:
            return -1
        elif needle == '':
            return 0
        else:
            for i in range(len(haystack)-len(needle) + 1):
                if haystack[i:len(needle)+i] == needle[:]:
                    return i
    def strStr2(self, haystack, needle):
        lenA, lenB = len(haystack), len(needle)
        if not lenB:
            return 0
        if lenB > lenA:
            return -1

        for i in range(lenA - lenB + 1):
            if haystack[i:i + lenB] == needle:
                return i
        return -1
    def strStr3(self, haystack, needle):
        if not needle:
            return 0
        left = 0 
        right = len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        return -1

class KMP(object):      
    def __init__(self, pat):
        self.pat = pat
        M = len(pat)
        self.dp = [[0 for _ in range(256)] for _ in range(M)]

        self.dp[0][ord(pat[0])] = 1
        X = 0
        for j in range(1, M):
            for c in range(256):
                self.dp[j][c] = self.dp[X][c]
            self.dp[j][ord(pat[j])] = j + 1
            X = self.dp[X][ord(pat[j])]
            
    def search(self, txt):
        M = len(self.pat)
        N = len(txt)
        # pat 的初始态为 0
        j = 0
        for i in range(N):
            # 当前是状态 j，遇到字符 txt[i]，
            # pat 应该转移到哪个状态？
            j = self.dp[j][ord(txt[i])]
            # 如果达到终止态，返回匹配开头的索引
            if j == M: return i - M + 1

        # 没到达终止态，匹配失败
        return -1

class TestSolution(unittest.TestCase):
    def test_0(self):
        haystack = "hello"
        needle = "ll"
        res = 2
        self.assertEqual(res, Solution().strStr3(haystack, needle))
    def test_1(self):
        haystack = ""
        needle = ""
        res = 0
        self.assertEqual(res, Solution().strStr3(haystack, needle))
    def test_2(self):
        haystack = "aaaaa"
        needle = "bba"
        res = -1
        self.assertEqual(res, Solution().strStr3(haystack, needle))

if __name__ == '__main__':
    unittest.main()
    
