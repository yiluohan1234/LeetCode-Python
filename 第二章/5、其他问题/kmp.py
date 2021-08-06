#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : kmp.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/03 15:01:38
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
KMP 算法（Knuth-Morris-Pratt 算法）字符串匹配算法
'''
import unittest
class kmp(object):
    def __init__(self, pat):
        m = len(pat)
        self.pat = pat 
        # dp[状态][字符] = 下个状态
        self.dp = [[0 for _ in range(256)] for _ in range(m)]
        # base case
        self.dp[0][ord(pat[0])] = 1
        # 影子状态 x 初始为 0
        x = 0
        # #当前状态 j 从 1 开始
        # for j in range(1, m):
        #     for c in range(0, 256):
        #         if ord(pat[j]) == c:
        #             self.dp[j][c] = j + 1
        #         else:
        #             self.dp[j][c] = self.dp[x][c];
        #     #更新影子状态
        #     x = self.dp[x][ord(pat[j])]
        # 构建状态转移图（稍改的更紧凑了）
        for j in range(1, m):
            for c in range(0, 256):
                self.dp[j][c] = self.dp[x][c]
            self.dp[j][ord(pat[j])] = j + 1
            # 更新影子状态:当前是状态 X，遇到字符 pat[j]，pat 应该转移到哪个状态？
            x = self.dp[x][ord(pat[j])]
    def search(self, txt):
        m = len(self.pat)
        n = len(txt)
        # pat 的初始态为 0
        j = 0
        for i in range(0, n):
            # 计算 pat 的下一个状态
            j = self.dp[j][ord(txt[i])]
            # 到达终止态，返回结果
            if j == m:
                return i - m + 1
        # 没到达终止态，匹配失败
        return -1
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        txt = "aaacaaab" 
        p = "aaab"
        res = 4
        self.assertEqual(res, kmp(p).search(txt))

    def test_1(self):
        txt = "aaaaaaab" 
        p = "aaab"
        res = 4
        self.assertEqual(res, kmp(p).search(txt))

    
if __name__ == '__main__':
    unittest.main()