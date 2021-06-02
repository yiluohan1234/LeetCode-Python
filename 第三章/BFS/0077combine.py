#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月20日
#    > description: 
#######################################################################
'''
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
'''
import unittest
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        path = []
        self.backtrack(n, k, 1, path)
        return self.res 
    def backtrack(self, n, k, start, path):
        if len(path) == k:
            self.res.append(path[:])
            return
        for i in range(start, n+1):
            path.append(i)
            self.backtrack(n, k, i+1, path)
            path.pop()



class TestSolution(unittest.TestCase):
    def test_0(self):
        n = 4
        k = 2
        res = [
          [1,2],
          [1,3],
          [1,4],
          [2,3],
          [2,4],
          [3,4],
        ]
        self.assertEqual(res, Solution().combine(n, k))

if __name__ == "__main__":
    unittest.main()
