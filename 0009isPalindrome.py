#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月17日
#######################################################################
'''
9. Palindrome Number
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
import unittest
class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res, y = 0, x
        while x :
            res = res * 10 + x % 10
            x  = x//10
        
        return  y == res
class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x != int(str(x)[::-1]):
            return False
        else:
            return True
class Solution3(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while x/div >= 10:
            div *= 10
        while x > 0:
            left = x / div
            right = x % 10
            if left != right:
                return False
            x = (x%div) / 10
            div = div / 100
        return True   

class Solution4(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #思考：这里大家可以思考一下，为什么末尾为 0 就可以直接返回 false
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10
        
        return x == revertedNumber or x == revertedNumber / 10
 
class TestSolution(unittest.TestCase):
    def test_s1_0(self):
        nums = 121
        res = True
        self.assertEqual(res, Solution1().isPalindrome(nums))
    def test_s1_1(self):
        nums = -121
        res = False
        self.assertEqual(res, Solution1().isPalindrome(nums))
    def test_s1_2(self):
        nums = 10
        res = False
        self.assertEqual(res, Solution1().isPalindrome(nums))
        
    def test_s2_0(self):
        nums = 121
        res = True
        self.assertEqual(res, Solution2().isPalindrome(nums))
    def test_s2_1(self):
        nums = -121
        res = False
        self.assertEqual(res, Solution2().isPalindrome(nums))
    def test_s2_2(self):
        nums = 10
        res = False
        self.assertEqual(res, Solution2().isPalindrome(nums))
    
    def test_s3_0(self):
        nums = 121
        res = True
        self.assertEqual(res, Solution3().isPalindrome(nums))
    def test_s3_1(self):
        nums = -121
        res = False
        self.assertEqual(res, Solution3().isPalindrome(nums))
    def test_s3_2(self):
        nums = 10
        res = False
        self.assertEqual(res, Solution3().isPalindrome(nums))
    
    def test_s4_0(self):
        nums = 121
        res = True
        self.assertEqual(res, Solution4().isPalindrome(nums))
    def test_s4_1(self):
        nums = -121
        res = False
        self.assertEqual(res, Solution4().isPalindrome(nums))
    def test_s4_2(self):
        nums = 10
        res = False
        self.assertEqual(res, Solution4().isPalindrome(nums))

if __name__ == "__main__":
    unittest.main()