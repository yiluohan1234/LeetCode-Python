#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年4月27日
#    > description: 
#######################################################################
'''
[1109. 航班预订统计](https://leetcode-cn.com/problems/corporate-flight-bookings/)
这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。
'''
import unittest
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        nums = [0 for _ in range(n)]
        df = Difference(nums)
        for b in bookings:
            i = b[0] - 1
            j = b[1] - 1
            val = b[2]
            df.increment(i, j, val)
        return df.result()
class Difference(object):     
    def __init__(self, nums):
        self.nums = nums
        self.diff = [nums[0]]
        for i in range(1, len(nums)):
            self.diff.append(nums[i] - nums[i-1])
    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.nums):
            self.diff[j+1] -= val

    def result(self):
        # diff[i] = nums[i] - nums[i-1]
        res = [self.diff[0]]
        for i in range(1, len(self.nums)):
            res.append(res[i-1] + self.diff[i])
        
        return res
class TestSolution(unittest.TestCase):
    def test_0(self):
        bookings = [[1,2,10],[2,3,20],[2,5,25]]
        n = 5
        res = [10,55,45,25,25]
        self.assertEqual(res, Solution().corpFlightBookings(bookings, n))
    def test_1(self):
        bookings = [[1,2,10],[2,2,15]]
        n = 2
        res = [10,25]
        self.assertEqual(res, Solution().corpFlightBookings(bookings, n))


if __name__ == "__main__":
    unittest.main()

