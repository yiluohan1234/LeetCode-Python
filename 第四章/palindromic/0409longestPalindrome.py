#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0409longestPalindrome.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/13 09:31:46
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
[409. 最长回文串](https://leetcode-cn.com/problems/longest-palindrome/)
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。

'''
import unittest
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_to_freq = {}
        res = 0

        for c in s:
            c_to_freq[c] = c_to_freq.get(c, 0) + 1

        for c,freq in c_to_freq.items():
            if freq % 2 == 0:
                # 如果出现个数为偶数，直接加入  
                res += freq
            else:
                # 如果为奇数，则加value - 1，并且，该字母的次数变为1
                res += freq - 1
                c_to_freq[k] = 1
        # 如果遍历完成的字符串中还有，出现值为1的字母，那么结果长度还要加1才行，因为可以把这个单个字母放在中间，使长度再增加1
        return res + 1 if 1 in c_to_freq.values() else res
    def longestPalindrome1(self, s):
        c_to_freq = {}

        for c in s:
            c_to_freq[c] = c_to_freq.get(c, 0) + 1

        is_ord = 0        #最多允许一个出现频率freq为奇数的字母，置于中间
        odd_freq_cnt = 0    #出现频率freq为奇数的字母个数
        for c, freq in c_to_freq.items():
            if freq % 2 == 1:
                is_ord = 1
                odd_freq_cnt += 1
        
        return len(s) - odd_freq_cnt + is_ord
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "abccccdd"
        res = 7
        self.assertEqual(res, Solution().longestPalindrome1(s))

if __name__ == "__main__":
    unittest.main()