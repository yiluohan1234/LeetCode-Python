#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0875minEatingSpeed.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/14 14:10:23
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
875. 爱吃香蕉的珂珂(https://leetcode-cn.com/problems/koko-eating-bananas/)
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
'''
import unittest
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.canEat(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo 
    
    def canEat(self, piles, h, k):
        total_time = 0
        for i in piles:
            total_time += (i + k - 1) // k
        return total_time <= h
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        piles = [3,6,7,11] 
        h = 8
        res = [3, 4]
        self.assertEqual(res, Solution().searchRange(piles, h))
    def test_1(self):
        piles = [30,11,23,4,20]
        h = 5
        res = 30
        self.assertEqual(res, Solution().searchRange(piles, h))

if __name__ == '__main__':
    #unittest.main()
    piles = [3,6,7,11]
    h = 8
    def canEat(piles, h, k):
        total_time = 0
        for i in range(len(piles)):
            if piles[i] < k:
                total_time += 1
            else:
                cur_time = piles[i] / k + 1
                total_time += cur_time
        print(total_time)
        return total_time >= h
    
    print(canEat(piles, 8, 4))