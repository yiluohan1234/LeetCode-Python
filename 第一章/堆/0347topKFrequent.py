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
347. 前 K 个高频元素(https://leetcode-cn.com/problems/top-k-frequent-elements/description/)

给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

'''
import unittest
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 遇到求前K的题目，内置的sorted和堆排序无脑安排上就对了
        # return [x[0] for x in sorted(Counter(nums).items(),key = lambda x: x[1],reverse=True)[:k]]
        import heapq
        from collections import Counter
        dic = Counter(nums)
        hq = []

        for num, freq in dic.items():
            if len(hq) < k:
                heapq.heappush(hq, (freq, num))
            else:
                if hq[0][0] < freq:
                    heapq.heappop(hq)
                    heapq.heappush(hq, (freq, num))
        
        return [x[1] for x in hq]
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1,1,1,2,2,3]
        k = 2
        res = [1,2]
        self.assertEqual(res, Solution().topKFrequent(nums, k))
    def test_1(self):
        nums = [1]
        k = 1
        res = [1]
        self.assertEqual(res, Solution().topKFrequent(nums, k))

if __name__ == '__main__':
    unittest.main()
    
