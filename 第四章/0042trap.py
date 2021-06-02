#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月11日
#    > description: 
#######################################################################
'''
[42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

'''
import unittest
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 双指针解法
        n = len(height)
        left, right = 0, n - 1
        l_max, r_max = height[0], height[n-1]
        res = 0
        
        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
            
        return res
    def trap1(self, height):
        # 暴力解法
        # 位置i能达到的水柱高度和其左边的最高柱子、右边的最高柱子有关.
        # 我们分别称这两个柱子高度为l_max和r_max；位置 i 最大的水柱高度就是min(l_max, r_max)。
        n = len(height)
        res = 0
        
        for i in range(1, n-1):
            l_max, r_max = 0, 0
            # 左边[0,i]
            for j in range(0, i+1):
                l_max = max(l_max, height[j])
            # 右边[i,n]
            for j in range(i, n):
                r_max = max(r_max, height[j])
            res += min(l_max, r_max) - height[i]
        
        return res
    def trap2(self, height):
        # 带备忘录的暴力解法
        # 位置i能达到的水柱高度和其左边的最高柱子、右边的最高柱子有关.
        # 设两个柱子高度为l_max和r_max；位置 i 最大的水柱高度就是min(l_max, r_max)。
        n = len(height)
        res = 0
        l_max = [0 for _ in range(n)]
        r_max = [0 for _ in range(n)]
        # base case
        l_max[0] = height[0]
        r_max[n-1] = height[n-1]
        # 从左向右计算 l_max
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])
        # 从右向左计算 r_max
        for i in range(n-2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])
        
        for i in range(1, n-1):
            res += min(l_max[i], r_max[i]) - height[i];
        
        return res
        
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [0,1,0,2,1,0,1,3,2,1,2,1]
        res = 6
        self.assertEqual(res, Solution().trap2(s))
    def test_1(self):
        s = [4,2,0,3,2,5]
        res = 9
        self.assertEqual(res, Solution().trap2(s))

if __name__ == "__main__":
    unittest.main()
