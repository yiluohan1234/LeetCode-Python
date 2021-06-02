#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年4月28日
#    > description: 
#######################################################################
'''
[292. Nim 游戏](https://leetcode-cn.com/problems/nim-game/)
你和你的朋友，两个人一起玩 Nim 游戏：

桌子上有一堆石头。
你们轮流进行自己的回合，你作为先手。
每一回合，轮到的人拿掉 1 - 3 块石头。
拿掉最后一块石头的人就是获胜者。
假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 n 的情况下赢得游戏。如果可以赢，返回 true；否则，返回 false 。
'''
import unittest
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n%4) != 0
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 4
        res = False
        self.assertEqual(res, Solution().canWinNim(s))

if __name__ == "__main__":
    unittest.main()
