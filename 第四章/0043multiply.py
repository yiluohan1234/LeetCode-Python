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
[43. 字符串相乘](https://leetcode-cn.com/problems/multiply-strings/)
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
'''
import unittest
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = [0 for _ in range(m+n)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = (ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'))
                p1, p2 = i+j, i+j+1
                sum = mul + res[p2]
                res[p2] = sum % 10
                res[p1] += sum // 10
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        ans = ""
        
        for c in range(i, len(res)):
            ans += str(res[c])
        return "0" if len(ans) == 0 else ans
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        num1 = "123"
        num2 = "456"
        res = "56088"
        self.assertEqual(res, Solution().multiply(num1, num2))
    def test_1(self):
        num1 = "2"
        num2 = "3"
        res = "6"
        self.assertEqual(res, Solution().multiply(num1, num2))

if __name__ == "__main__":
    unittest.main()
