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
[241. 为运算表达式设计优先级](https://leetcode-cn.com/problems/different-ways-to-add-parentheses/)
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
'''
import unittest
class Solution(object):
    def __init__(self):
        self.momo = {}
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # 避免重复计算
        if expression in self.momo:
            return self.momo[expression]
        res = []
        for i in range(len(expression)):
            c = expression[i]
            if c == '-' or c == '+' or c == '*':
                left = self.diffWaysToCompute(expression[0:i])
                right = self.diffWaysToCompute(expression[i+1:])
            
                for a in left:
                    for b in right:
                        if c == '-':
                            res.append(a - b)
                        if c == '+':
                            res.append(a + b)
                        if c == '*':
                            res.append(a * b)
        
        if not res:
            res.append(int(expression))
        
        # 将结果添加进备忘录
        self.momo[expression] = res
        return res
                            
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "2*3-4*5"
        res = [-34, -10, -14, -10, 10]
        self.assertEqual(res, Solution().diffWaysToCompute(s))
    def test_1(self):
        s = "2-1-1"
        res = [2, 0]
        self.assertEqual(res, Solution().diffWaysToCompute(s))
if __name__ == "__main__":
    unittest.main()
