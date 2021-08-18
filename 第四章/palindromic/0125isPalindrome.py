#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0125isPalindrome.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/12 16:20:56
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
[125. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

 
'''
import unittest
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # trans_s = ""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         trans_s += s[i].lower()
        trans_s = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(trans_s) - 1
        while left < right:
            if trans_s[left] != trans_s[right]:
                return False 
            left += 1
            right -= 1
        
        return True
    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        trans_s = "".join(ch.lower() for ch in s if ch.isalnum())
        return trans_s == trans_s[::-1]
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "A man, a plan, a canal: Panama"
        res = True
        self.assertEqual(res, Solution().isPalindrome(s))

if __name__ == "__main__":
    unittest.main()