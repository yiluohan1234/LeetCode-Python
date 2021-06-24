#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 1046lastStoneWeight.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/06/24 12:28:30
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
[1046. 最后一块石头的重量](https://leetcode-cn.com/problems/last-stone-weight/)
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

由于Python不支持大根堆，所以我们需要在预处理的时候，将所有数据转为负数用于适配小根堆。
'''

import unittest
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            if one != two:
                heapq.heappush(stones, one - two)
        
        return -stones[0] if stones else 0

       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [2, 3, 1, 0, 2, 5, 3]
        res = [2, 3]
        self.assertEqual(res, Solution().lastStoneWeight(s))

if __name__ == '__main__':
    unittest.main()
    
