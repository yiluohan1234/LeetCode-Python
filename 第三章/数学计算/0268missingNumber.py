#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月19日
#    > description: 
#######################################################################
'''
[268. 丢失的数字](https://leetcode-cn.com/problems/missing-number/)
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

进阶：
你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
'''
import unittest
class Solution(object):
    def missingNumber(self, nums):
        """
        :type num: int
        :rtype: str
        """ 
        # n^n=0, n^0=n
        n = len(nums)
        res = 0
        res ^= n
        for i in range(len(nums)):
            res ^= i ^nums[i]
        
        return res
    
    def missingNumber1(self, nums):
        """
        :type num: int
        :rtype: str
        """ 
        # 等差数列：missingNum = sum(1,..n) - sum(nums),expect = (0+n)*(n+1)/2(存在溢出风险)
        n = len(nums)
        res = 0
        res += n - 0
        for i in range(len(nums)):
            res += i - nums[i]
        
        return res
        
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [3, 0, 1]
        res = 2
        self.assertEqual(res, Solution().missingNumber1(s))
    def test_1(self):
        s = [0,1]
        res = 2
        self.assertEqual(res, Solution().missingNumber1(s))
    def test_2(self):
        s = [9,6,4,2,3,5,7,0,1]
        res = 8
        self.assertEqual(res, Solution().missingNumber1(s))
    def test_3(self):
        s = [0]
        res = 1
        self.assertEqual(res, Solution().missingNumber1(s))

if __name__ == "__main__":
    unittest.main()
