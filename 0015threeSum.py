#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月24日
#    > description: 
#######################################################################
'''
15. 3Sum
Given an array nums of n integers, 
are there elements a, b, c in nums 
such that a + b + c = 0? 
Find all unique triplets in the array 
which gives the sum of zero.

Notice that the solution set must not 
contain duplicate triplets.

 

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
'''
import unittest
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums.sort()#[-2,0,1,1,2]
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r= i + 1, n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif tmp > 0:
                    r -= 1
                else:
                    l += 1
                    
        return res
     
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [-1,0,1,2,-1,-4]
        res = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(res, Solution().threeSum(s))
    def test_2(self):
        s = []
        res = []
        self.assertEqual(res, Solution().threeSum(s))
    def test_3(self):
        s = [0]
        res = []
        self.assertEqual(res, Solution().threeSum(s))
    def test_4(self):
        s = [-2,0,1,1,2]
        res = [[-2,0,2],[-2,1,1]]
        self.assertEqual(res, Solution().threeSum(s))
if __name__ == "__main__":
    unittest.main()
