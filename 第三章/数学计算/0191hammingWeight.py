#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2021年4月28日
#    > description: 
#######################################################################
'''
[191. 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/)
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
'''
import unittest
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 0:
            n = n & (n - 1)
            res += 1
        
        return res
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = int("00000000000000000000000000001011", 2)
        res = 3
        self.assertEqual(res, Solution().hammingWeight(s))

if __name__ == "__main__":
    unittest.main()
