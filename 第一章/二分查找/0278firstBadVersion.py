#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0278firstBadVersion.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/14 13:22:31
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
278. 第一个错误的版本(https://leetcode-cn.com/problems/first-bad-version/)
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
'''
import unittest
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n 
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        
        return lo
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [5,7,7,8,8,10]
        target = 8
        res = [3, 4]
        self.assertEqual(res, Solution().searchRange(nums, target))
    def test_1(self):
        nums = [5,7,7,8,8,10]
        target = 6
        res = [-1, -1]
        self.assertEqual(res, Solution().searchRange(nums, target))

if __name__ == '__main__':
    unittest.main()
    
