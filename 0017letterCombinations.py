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
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
import unittest
class Solution(object):
    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []
        
        def backtrack(digits, combination):
            if len(digits) == 0:
                res.append(combination)
            else:
                for alphabet in phone[digits[0]]:
                    backtrack(digits[1:], combination + alphabet)
        if digits:
            backtrack(digits, '')
        return res
class Solution2(object):
    def __init__(self):
        self.res = []
        self.mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        self.recursion(digits, 0, "")
        return self.res
    
    def recursion(self, digits: str, index: int, word: str):
        if index == len(digits):
            self.res.append(word)
            return
        for s in self.mapping[digits[index]]:
            word += s
            self.recursion(digits, index+1, word)
            word = word[:-1]
class Solution3(object):
    def letterCombinations(self, digits):
        di={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def helper(ans,digits,di,index):
            if index>=len(digits):
                if len(ans)>0:
                    yield ans
                else:
                    return
            else:
                s=digits[index]
                ss=di[s]
                for i in ss:
                    yield from helper(ans+i,digits,di,index+1)
        return list(helper("",digits,di,0))

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "23"
        res = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(res, Solution().letterCombinations(s))

if __name__ == "__main__":
    unittest.main()