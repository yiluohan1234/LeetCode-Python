#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################

import unittest
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        window, need = {}, {}
        left, right = 0, 0
        for c in p:
            need[c] = need.get(c, 0) + 1
        valid = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            print("window: [%d, %d)\n", left, right)
            while right - left >= len(p):
                if valid == len(need):
                    print("success:%d", left)
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        return res
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "cbaebabacd" 
        p = "abc"
        res = [0,6]
        self.assertEqual(res, Solution().findAnagrams(s, p))

if __name__ == "__main__":
    unittest.main()
