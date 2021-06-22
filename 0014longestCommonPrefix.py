#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################
'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
import unittest
class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix) 
class Solution2(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        
        for letters in zip(*strs):
            if len(set(letters)) != 1:
                return prefix
            prefix += letters[0]
                
        return prefix        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = ["flower","flow","flight"]
        res = "fl"
        self.assertEqual(res, Solution1().longestCommonPrefix(s))
    def test_1(self):
        s = ["dog","racecar","car"]
        res = ""
        self.assertEqual(res, Solution1().longestCommonPrefix(s))
    def test1_0(self):
        s = ["flower","flow","flight"]
        res = "fl"
        self.assertEqual(res, Solution2().longestCommonPrefix(s))
    def test1_1(self):
        s = ["dog","racecar","car"]
        res = ""
        self.assertEqual(res, Solution2().longestCommonPrefix(s))

if __name__ == "__main__":
    unittest.main()