#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: 崔羽飞
#    > Mail: XXX@qq.com
#    > Created Time: 2021年4月28日
#    > description: 
#######################################################################
'''
(793. 阶乘函数后 K 个零)[https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function/]
 
f(x) 是 x! 末尾是 0 的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 ）
 
例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。
给定 K，找出多少个非负整数 x ，能满足 f(x) = K 。
 
'''
import unittest
import sys
INT_MAX = sys.maxsize
class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        return self.right_bound(K) - self.left_bound(K) + 1
    def left_bound(self, K):
        lo, hi = 0, INT_MAX
        while lo < hi:
            mid = lo + (hi - lo)/2
            if self.trailingZeroes(mid) < K:
                lo = mid + 1
            elif self.trailingZeroes(mid) > K:
                hi = mid
            else:
                hi = mid
        
        return lo
    def right_bound(self, K):
        lo, hi = 0, INT_MAX
        while lo < hi:
            mid = lo + (hi - lo)/2
            if self.trailingZeroes(mid) < K:
                lo = mid + 1
            elif self.trailingZeroes(mid) > K:
                hi = mid
            else:
                lo = mid + 1
        
        return lo - 1
                
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        dividor = 5
        while dividor <= n:
            res += n/dividor
            dividor *= 5
        return res
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 0
        res = 5
        self.assertEqual(res, Solution().preimageSizeFZF(s))

if __name__ == "__main__":
    unittest.main()
