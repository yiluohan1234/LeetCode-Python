#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 1845SeatManager.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/06/24 12:24:41
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
[面试题 17.14. 最小K个数](https://leetcode-cn.com/problems/smallest-k-lcci/)
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
'''
import unittest
import heapq
class Solution:
    def smallestK1(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 小根堆：每次获取的数据都无脑入堆，然后最终将前K个数字返回
        # 大根堆：仅维护K个长度的堆，由于python没有，需要入负值，如果当前的数大于heap[0]，则堆顶出堆，当前数入堆，最终返回。
        hq = []
        for i in arr:
            if len(hq) < k:
                heapq.heappush(hq, -i)
            else:
                if hq[0] < -i:
                    heapq.heappop(hq)
                    heapq.heappush(hq, -i)
        return [-i for i in hq]
    def smallestK(self, arr, k):
        hq = []
        for i in arr:
            heapq.heappush(hq, i)
           
        return hq
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        arr = [1,3,5,7,2,4,6,8]
        k = 4
        res = [1,2,3,4]
        self.assertEqual(res, Solution().smallestK1(arr, k))

if __name__ == '__main__':
    unittest.main()
    
