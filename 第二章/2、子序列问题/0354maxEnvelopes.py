#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月20日
#    > description: 
#######################################################################
'''
[354. 俄罗斯套娃信封问题](https://leetcode-cn.com/problems/russian-doll-envelopes/)
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
注意：不允许旋转信封。
这个解法的关键在于，对于宽度w相同的数对，要对其高度h进行降序排序。
因为两个宽度相同的信封不能相互包含的，而逆序排序保证在w相同的数对中最多只选取一个计入 LIS。
'''
import unittest
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = sorted(envelopes, key = lambda x:(x[0], -x[1]))
        height = [0 for _ in range(len(envelopes))]
        for i in range(len(envelopes)):
            height[i] = envelopes[i][1]
        
        return self.lengthOfLIS(height)
        
    
    def lengthOfLIS(self, nums):
        piles = 0
        n = len(nums)
        top = [0 for _ in range(n)]
        for i in range(n):
            poker = nums[i]
            lo, hi = 0, piles 
            while lo < hi:
                mid = (lo + hi) // 2
                if top[mid] >= poker:
                    hi = mid
                else:
                    lo = mid + 1
            if lo == piles:
                piles += 1
            top[lo] = poker
        
        return piles

class TestSolution(unittest.TestCase):
    def test_0(self):
        envelopes = [[5,4],[6,4],[6,7],[2,3]]
        res = 3
        self.assertEqual(res, Solution().maxEnvelopes(envelopes))
    def test_1(self):
        envelopes = [[1,1],[1,1],[1,1]]
        res = 1
        self.assertEqual(res, Solution().maxEnvelopes(envelopes))

if __name__ == "__main__":
    unittest.main()
