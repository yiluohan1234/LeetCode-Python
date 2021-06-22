#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月27日
#    > description: 
#######################################################################
'''
18. 4Sum
Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
import unittest
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:   # 因为j=i+1这个元素会直接往下执行
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    if target == tmp:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif tmp > target:
                        r -= 1
                    else:
                        l += 1
        return res
class Solution2(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.helper(nums, target, 4, [], results)
        return results
    
    def helper(self, nums, target, N, res, results):
        
        if len(nums) < N or N < 2: #1
            return
        if N == 2: #2
            output_2sum = self.twoSum(nums, target)
            if output_2sum != []:
                for idx in output_2sum:
                    results.append(res + idx)
        
        else: 
            for i in range(len(nums) -N +1): #3
                if nums[i]*N > target or nums[-1]*N < target: #4
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]: #5
                    self.helper(nums[i+1:], target-nums[i], N-1, res + [nums[i]], results)
    
    
    def twoSum(self, nums, target):
        res = []
        left = 0
        right = len(nums) - 1 
        while left < right: 
            temp_sum = nums[left] + nums[right] 

            if temp_sum == target:
                res.append([nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while right > left and nums[right] == nums[right + 1]:
                    right -= 1
                                
            elif temp_sum < target: 
                left +=1 
            else: 
                right -= 1
                                        
        return res      
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        res = [
          [-2, -1, 1, 2],
          [-2,  0, 0, 2],
          [-1,  0, 0, 1]
        ]
        self.assertEqual(res, Solution2().fourSum(nums, target))
    def test_1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        res = [
          [-2, -1, 1, 2],
          [-2,  0, 0, 2],
          [-1,  0, 0, 1]
        ]
        self.assertEqual(res, Solution().fourSum(nums, target))
    def test_2(self):
        nums = [-3,-2,-1,0,0,1,2,3]
        target = 0
        res = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        self.assertEqual(res, Solution().fourSum(nums, target))


if __name__ == "__main__":
    unittest.main()