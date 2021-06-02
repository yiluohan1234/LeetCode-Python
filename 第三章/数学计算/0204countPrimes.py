#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年4月30日
#    > description: 
#######################################################################
'''
204. [Count Primes](https://leetcode.com/problems/count-primes/)
Count the number of prime numbers less than a non-negative number, n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
204. [计数质数](https://leetcode-cn.com/problems/count-primes/)
统计所有小于非负整数 n 的质数的数量。

'''

import unittest
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isprime = [True for _ in range(n)]
        for i in range(2, n):
            if i*i >= n:
                break
            if isprime[i]:
                for j in range(i*i, n, i):
                    isprime[j] = False
        res = 0
        for i in range(2, n):
            if isprime[i]:
                res += 1
        
        return res
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n):
            if self.isprime(i):
                res += 1
        return res
    def isprime(self, n):
        #  for (int i = 2; i * i <= n; i++)
        for i in range(2, n):
            if i*i > n:
                break
            if n % i == 0:
                return False 
        return True
    
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 10
        res = 4
        self.assertEqual(res, Solution().countPrimes(s))

if __name__ == "__main__":
    unittest.main()
