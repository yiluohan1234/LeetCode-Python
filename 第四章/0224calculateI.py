#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年4月28日
#    > description: 
#######################################################################
'''
[224. 基本计算器](https://leetcode-cn.com/problems/basic-calculator/)
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

示例 1：
输入：s = "1 + 1"
输出：2
示例 2：
输入：s = " 2-1 + 2 "
输出：3
示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
'''
import unittest
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(s):
            stack = []
            num = 0
            sign = '+'
            # s的长度大于0才能进行如下操作
            while len(s) > 0:
                c = s.pop(0)
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    num = helper(s)
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        stack[-1] = int(stack[-1]/float(num))
                    num = 0
                    sign = c
                if c == ')':
                    break
            
            return sum(stack)
        return helper(list(s))
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "1 + 1"
        res = 2
        self.assertEqual(res, Solution().calculate(s))
    def test_1(self):
        s = " 2-1 + 2 "
        res = 3
        self.assertEqual(res, Solution().calculate(s))
    def test_2(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        res = 23
        self.assertEqual(res, Solution().calculate(s))
    def test_3(self):
        s = "1+(3+2*2)-2*3/(2+2)"
        res = 7
        self.assertEqual(res, Solution().calculate(s))

if __name__ == "__main__":
    unittest.main()
