#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月12日
#    > description: 
#######################################################################
'''
[20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
'''
import unittest
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) and self.leftOf(c) == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
    def leftOf(self, c):
        if c== ']':
            return '['
        elif c == ')':
            return '('
        else:
            return '{'
    def isValid1(self, s):
        # 如果只有一种符号()
        # 待匹配的左括号数量
        left = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                left -= 1
            if left < 0:
                return False
        
        return left == 0

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "()"
        res = True
        self.assertEqual(res, Solution().isValid(s))
    def test_1(self):
        s = "()[]{}"
        res = True
        self.assertEqual(res, Solution().isValid(s))
    def test_2(self):
        s = "(]"
        res = False
        self.assertEqual(res, Solution().isValid(s))

if __name__ == "__main__":
    unittest.main()
