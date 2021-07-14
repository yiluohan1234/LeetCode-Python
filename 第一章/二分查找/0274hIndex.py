#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0274hIndex.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/13 10:19:58
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
274. H 指数(https://leetcode-cn.com/problems/h-index/)
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。
h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。
例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
'''
# [0, 1, 3, 5, 6]
import unittest
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # 275 注释排序
        # 如果citations[index] >= length - index，表示为满足题意的
        citations.sort()
        n = len(citations)
        
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if citations[mid] >= n - mid:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return n - lo
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [3,0,6,1,5]
        res = 3
        self.assertEqual(res, Solution().hIndex(s))
    def test_1(self):
        s = [1,3,1]
        res = 1
        self.assertEqual(res, Solution().hIndex(s))

if __name__ == '__main__':
    unittest.main()
    
