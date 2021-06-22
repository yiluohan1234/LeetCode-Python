#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月9日
#######################################################################
import unittest
"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lens = len(nums1) + len(nums2)
        if lens % 2 == 1:
            return self.findKth(nums1, nums2, lens/2 + 1)
        else:
            n1 = self.findKth(nums1, nums2, lens/2)
            n2 = self.findKth(nums1, nums2, lens/2 + 1)
            return (n1 + n2)/2.0
    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k-1]
        if len(B) == 0:
            return A[k-1]
        if k == 1:
            return min(A[0], B[0])
        
        a = A[k/2 -1] if len(A) >= k/2 else None
        b = B[k/2 -1] if len(B) >= k/2 else None
        
        if b is None or (a is not None and a < b):
            return self.findKth(A[k/2:], B, k - k/2)
        else:
            return self.findKth(A, B[k/2:], k - k/2)
class TestSolution(unittest.TestCase):
    def test_s1_0(self):
        nums1 = [1,3]
        nums2 = [2]
        res = 2.00000
        self.assertEqual(res, Solution().findMedianSortedArrays(nums1, nums2))

    def test_s1_1(self):
        nums1 = [1,2]
        nums2 = [3,4]
        res = 2.50000
        self.assertEqual(res, Solution().findMedianSortedArrays(nums1, nums2))
    def test_s1_2(self):
        nums1 = [0,0]
        nums2 = [0,0]
        res = 0.00000
        self.assertEqual(res, Solution().findMedianSortedArrays(nums1, nums2))
    def test_s1_3(self):
        nums1 = []
        nums2 = [1]
        res = 1.00000
        self.assertEqual(res, Solution().findMedianSortedArrays(nums1, nums2))

    def test_s2_1(self):
        nums1 = [2]
        nums2 = []
        res = 2.00000
        self.assertEqual(res, Solution().findMedianSortedArrays(nums1, nums2))

if __name__ == "__main__":
    unittest.main()
# if __name__ == "__main__":
#     nums1 = [1,3]
#     nums2 = [2]
#     s = Solution()
#     print s.findMedianSortedArrays(nums1, nums2)