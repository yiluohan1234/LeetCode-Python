#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################
'''
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
import unittest
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, maxArea = 0, len(height) - 1, 0
        while left < right:
            area = (right - left)*min(height[left], height[right])
            maxArea = max(maxArea,area)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxArea
class TestSolution(unittest.TestCase):
    def test_none_0(self):
        nums = [1,8,6,2,5,4,8,3,7]
        res = 49
        self.assertEqual(res, Solution().maxArea(nums))

   

if __name__ == "__main__":
    unittest.main()