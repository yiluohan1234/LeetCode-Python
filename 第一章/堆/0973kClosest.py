#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0973kClosest.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/06/30 13:42:01
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
973. 最接近原点的 K 个点(https://leetcode-cn.com/problems/k-closest-points-to-origin/description/)
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
'''
import unittest
import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # 遇到求前K的题目，内置的sorted和堆排序无脑安排上就对了
        # 小顶堆实现大顶堆：入堆为负，比较小于负
        import heapq
        hp = []
        for point in points:
            distance = sum(map(lambda x: abs(x ** 2), point))
            if len(hp) < k:
                heapq.heappush(hp, [-distance, point])
            else:
                if hp[0][0] < -distance:
                    heapq.heappop(hp)
                    heapq.heappush(hp, [-distance, point])
        return [point for distance, point in hp]
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        points = [[1,3],[-2,2]]
        k = 1
        res = [[-2,2]]
        self.assertEqual(res, Solution().kClosest(points, k))
    def test_1(self):
        points = [[3,3],[5,-1],[-2,4]]
        k = 2
        res = [[3,3],[-2,4]]
        self.assertEqual(res, Solution().kClosest(points, k))

if __name__ == '__main__':
    unittest.main()
    
