#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月28日
#    > description: 
#######################################################################
'''
[435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:
可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

'''
import unittest
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intvs = sorted(intervals, key= lambda x:x[1])
        count = 1
        start_end = intvs[0][1]
        for num in intvs:
            start = num[0]
            end = num[1]
            if start >= start_end:
                count += 1
                start_end = end
        
        return len(intervals) - count
    def intervalSchedule(self, intervals):
        # 计算intervals的区间中，含有n个不重叠的子区间
        intvs = sorted(intervals, key= lambda x:x[1])
        count = 1
        start_end = intvs[0][1]
        for num in intvs:
            start = num[0]
            end = num[1]
            if start >= start_end:
                count += 1
                start_end = end
        
        return count
                
class TestSolution(unittest.TestCase):
    def test_0(self):
        s =  [[1,2], [2,3], [3,4], [1,3]]
        res = 1
        self.assertEqual(res, Solution().eraseOverlapIntervals(s))
    def test_1(self):
        s =  [[1,2], [1,2], [1,2]]
        res = 2
        self.assertEqual(res, Solution().eraseOverlapIntervals(s))
    def test_2(self):
        s =  [[1,2], [2,3]]
        res = 0
        self.assertEqual(res, Solution().eraseOverlapIntervals(s))

if __name__ == '__main__':
    unittest.main()