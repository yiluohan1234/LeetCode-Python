#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月13日
#    > description: 
#######################################################################
'''
392. 判断子序列(https://leetcode-cn.com/problems/is-subsequence/)
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
进阶：
如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
致谢：
特别感谢 @pbrother 添加此问题并且创建所有测试用例。

示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false
'''
import unittest
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)
    
    def isSubsequence1(self, s, t):
        idx = {}
        for i in range(len(t)):
            c = t[i]
            idx.setdefault(c, []).append(i)
        j = 0
        for i in range(len(s)):
            c = s[i]
            if c not in idx:
                return False
            pos = self.left_BST(idx[c], j)
            if pos == len(idx[c]):
                return False
            j = idx[c][pos] + 1
        
        return True
    def left_BST(self, nums, val):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo)//2
            if val > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
            
        return lo
            
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "abc"
        t = "cacbhbc"
        res = True
        self.assertEqual(res, Solution().isSubsequence1(s, t))
    def test_1(self):
        s = "axc"
        t = "ahbgdc"
        res = False
        self.assertEqual(res, Solution().isSubsequence1(s, t))

if __name__ == "__main__":
    unittest.main()
