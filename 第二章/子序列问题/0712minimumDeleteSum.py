#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月25日
#    > description: 
#######################################################################
'''
[712. 两个字符串的最小ASCII删除和](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/)
给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。

示例 1:
输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
'''
import unittest
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # 定义：将 s1[i..] 和 s2[j..] 删除成相同字符串，最小的 ASCII 码之和为 dp(s1, i, s2, j)。
        m, n = len(s1), len(s2)
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dp(s1, 0, s2, 0)
    def dp(self, s1, i, s2, j):
        res = 0;
        # base case
        if i == len(s1):
            # 如果 s1 到头了，那么 s2 剩下的都得删除
            for m in range(j, len(s2)):
                res += ord(s2[m])
            return res

        if j == len(s2):
            # 如果 s2 到头了，那么 s1 剩下的都得删除    
            for n in range(i, len(s1)):
                res += ord(s1[n])
            return res

        if self.memo[i][j] != -1:
            return self.memo[i][j]
        if s1[i] == s2[j]:
            # s1[i] 和 s2[j] 都是在 lcs 中的，不用删除
            self.memo[i][j] = self.dp(s1, i+1, s2, j+1)
        else:
            # s1[i] 和 s2[j] 至少有一个不在 lcs 中，删一个
            self.memo[i][j] = min(ord(s1[i]) + self.dp(s1, i+1, s2, j), 
                                  ord(s2[j]) + self.dp(s1, i, s2, j+1))
        
        return self.memo[i][j]
class TestSolution(unittest.TestCase):
    def test_0(self):
        s1 = "sea"
        s2 = "eat"
        res = 231
        self.assertEqual(res, Solution().minimumDeleteSum(s1, s2))
    def test_1(self):
        s1 = "delete"
        s2 = "leet"
        res = 403
        self.assertEqual(res, Solution().minimumDeleteSum(s1, s2))
    

if __name__ == "__main__":
    unittest.main()
