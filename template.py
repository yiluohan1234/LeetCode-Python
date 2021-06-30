#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月3日
#    > description: 
#######################################################################
import unittest
import heapq
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [2, 3, 1, 0, 2, 5, 3]
        res = [2, 3]
        self.assertEqual(res, Solution().findRepeatNumber(s))

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    from collections import Counter
    dic = Counter(nums)
    print(dict(dic))
        
