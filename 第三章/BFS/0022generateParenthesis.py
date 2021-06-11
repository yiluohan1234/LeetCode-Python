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
[22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
输入：n = 1
输出：["()"]
'''
import unittest
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path = []
        self.res = []
        self.backtrack(n, n, path)
        return self.res
    # 可用的左括号为left个，可用的右括号为right个
    def backtrack(self, left, right, path):
        # 左括号剩下的多，不合法。因为是先去操作的左括号。
        if left > right:
            return
        # 数量小于0， 不合法
        if left < 0 or right < 0:
            return 
        # 当所有括号都恰好用完时，得到一个合法的括号组合
        if left == 0 and right == 0:
            self.res.append("".join(path))
            return
        # 尝试放一个左括号
        path.append('(')
        self.backtrack(left - 1, right, path)
        path.pop()
        
        # 尝试放一个右括号
        path.append(')')
        self.backtrack(left, right - 1, path)
        path.pop()
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1
        res = ["()"]
        self.assertEqual(res, Solution().generateParenthesis(s))
    def test_1(self):
        s = 3
        res = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(res, Solution().generateParenthesis(s))

if __name__ == "__main__":
    unittest.main()

