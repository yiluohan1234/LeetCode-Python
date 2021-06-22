#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月9日
#######################################################################
import unittest
"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
"""
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 0:
            return 0
        
        l, start, maps = 0, 0, {}
        for i in range(len(s)):
            start = max(start, maps.get(s[i], -1) + 1)
            l = max(l, i - start + 1)
            maps[s[i]] = i
        return l
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int,pwwkew
        """   
        if not s or len(s) == 0:
            return 0
        l, r, res = 0, 0, 0
        lookup = set()
        while l < len(s) and r < len(s):
            if s[r] not in lookup:
                lookup.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                lookup.discard(s[l])
                l += 1
        return res
class TestSolution(unittest.TestCase):
    def test_s1_0(self):
        s = "abcabcbb"
        res = 3
        self.assertEqual(res, Solution1().lengthOfLongestSubstring(s))

    def test_s1_1(self):
        s = "bbbbb"
        res = 1
        self.assertEqual(res, Solution1().lengthOfLongestSubstring(s))
    def test_s1_2(self):
        s = "pwwkew"
        res = 3
        self.assertEqual(res, Solution1().lengthOfLongestSubstring(s))
    def test_s1_3(self):
        s = ""
        res = 0
        self.assertEqual(res, Solution1().lengthOfLongestSubstring(s))
    def test_s2_0(self):
        s = "abcabcbb"
        res = 3
        self.assertEqual(res, Solution2().lengthOfLongestSubstring(s))

    def test_s2_1(self):
        s = "bbbbb"
        res = 1
        self.assertEqual(res, Solution2().lengthOfLongestSubstring(s))
    def test_s2_2(self):
        s = "pwwkew"
        res = 3
        self.assertEqual(res, Solution2().lengthOfLongestSubstring(s))
    def test_s2_3(self):
        s = ""
        res = 0
        self.assertEqual(res, Solution2().lengthOfLongestSubstring(s))

if __name__ == "__main__":
    unittest.main()
