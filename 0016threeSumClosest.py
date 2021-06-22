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
16. 3Sum Closest
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

 
Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''
import unittest
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n, res, diff = len(nums), None, float('inf')
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return target
                elif tmp > target:
                    r -= 1
                    if abs(tmp - target) < diff:
                        diff = abs(tmp - target)
                        res = tmp
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    if abs(tmp - target) < diff:
                        diff = abs(tmp - target)
                        res = tmp
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [-1,2,1,-4]
        target = 1
        res = 2
        self.assertEqual(res, Solution().threeSumClosest(nums, target))
    def test_1(self):
        nums = [1,2,4,8,16,32,64,128]
        target = 82
        res = 82
        self.assertEqual(res, Solution().threeSumClosest(nums, target))

if __name__ == "__main__":
    unittest.main()