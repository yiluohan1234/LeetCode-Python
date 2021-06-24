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
[1845. 座位预约管理系统](https://leetcode-cn.com/problems/seat-reservation-manager/)
请你设计一个管理 n 个座位预约的系统，座位编号从 1 到 n 。

请你实现 SeatManager 类：

SeatManager(int n) 初始化一个 SeatManager 对象，它管理从 1 到 n 编号的 n 个座位。所有座位初始都是可预约的。
int reserve() 返回可以预约座位的 最小编号 ，此座位变为不可预约。
void unreserve(int seatNumber) 将给定编号 seatNumber 对应的座位变成可以预约。
'''
import unittest
import heapq
class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.ret = [i for i in range(1, n+1)]

    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.ret)
        

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.ret, seatNumber)
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [2, 3, 1, 0, 2, 5, 3]
        res = [2, 3]
        self.assertEqual(res, Solution().findRepeatNumber(s))

if __name__ == '__main__':
    unittest.main()
    
