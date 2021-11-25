#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: findKthLargest.py
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2021年5月10日
#    > description: 
#######################################################################
'''
[215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
'''
import unittest
from queue import PriorityQueue
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.shuffle(nums)
        lo, hi = 0, len(nums) - 1
        # 索引转化
        idx = len(nums) - k 
        while lo <= hi:
            p = self.partition(nums, lo, hi)
            if p < idx:
                lo = p + 1
            elif p > idx:
                hi = p - 1
            else:
                return nums[p]
        
        return -1
    def partition(self, nums, lo, hi):
        if lo == hi:
            return lo
        
        mid = nums[lo]
        while lo < hi:
            while lo < hi and nums[hi] > mid:
                hi -= 1
            nums[lo] = nums[hi]
            while lo < hi and nums[lo] <= mid:
                lo += 1
            nums[hi] = nums[lo]
        nums[lo] = mid
        return lo 
    # 对数组元素进行随机打乱
    def shuffle(self, nums):
        n = len(nums)
        for i in range(n):
            # 从 i 到最后随机选一个元素
            r = i + random.randint(0, n - i - 1)
            # swap(nums, i, r)
            tmp = nums[i]
            nums[i] = nums[r]
            nums[r] = tmp 
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # PriorityQueue是优先级队列。越小的优先级越高，会被先取出。
        pq = PriorityQueue()
        for n in nums:
            pq.put(n)
            if pq.qsize() > k:
                pq.get()
        
        return pq.get()
    def quicksort(self, nums, lo, hi):
        if lo >= hi:
            return
        p = self.partition(nums, lo, hi)
        self.quicksort(nums, lo, p-1)
        self.quicksort(nums, p+1,hi)
        return nums

class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [3,1,2,5,4]
        k = 2
        res = 4
        self.assertEqual(res, Solution().findKthLargest(nums, k))
    def test_1(self):
        nums = [3,2,1,5,6,4]
        k = 2
        res = 5
        self.assertEqual(res, Solution().findKthLargest(nums, k))

if __name__ == "__main__":
    unittest.main()