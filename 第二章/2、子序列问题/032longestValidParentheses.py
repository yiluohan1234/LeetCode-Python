#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月24日
#    > description: 
#######################################################################
'''

'''
import unittest
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        stack = []

        for i in range(0, n):
            if s[i] == '(':
                stack.append(s[i])
                if i - 1 < 0:
                    continue
                dp[i] = dp[i-1]
            else:
                if len(stack) != 0:
                    stack.pop()
                    dp[i] = dp[i-1] + 2
                else:
                    if i - 1 < 0:
                        continue
                    dp[i] = dp[i-1]
        return dp[n-1]

    
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = "(()"
        res = 2
        self.assertEqual(res, Solution().longestValidParentheses(nums))
    def test_1(self):
        nums = ")()())"
        res = 4
        self.assertEqual(res, Solution().longestValidParentheses(nums))
    def test_2(self):
        nums = ""
        res = 0
        self.assertEqual(res, Solution().longestValidParentheses(nums))
    def test_3(self):
        nums = "()(())"
        res = 6
        self.assertEqual(res, Solution().longestValidParentheses(nums))

if __name__ == "__main__":
    unittest.main()
    0,1,2,3,4,5
    0,2,2,2,4,6

